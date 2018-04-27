/*
	Red-black Gauss-Seidel implemented in serial, applied to solve the matrix
	equation Ax=b where element of b is equal to one and A is a tridiagonal
	square matrix with values of -2 along the diagonal, +1 either side of the
	diagonal, and zero everywhere else.

	Since this code is in serial, you can compile using the normal C compiler,
	with the -lm flag since it uses the maths library routine sqrt():

	cc -Wall -lm -o <executable> coursework1.c

	and then simply ./<executable> from the shell to execute. When you extend this
	code to run in parallel, you will need to compile with mpicc (still with -lm),
	and run with mpirun as explained in Worksheet 0.

	Note I use here the single-block allocation model for the matrix A, which can
	then be referenced using A[i*N+j] in place of A[i][j]. This allows several rows
	of the matrix to be communicated at once when implementing the parallel version.
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>			/* Needed for sqrt(); compile with -lm. */
#include <mpi.h>

/* Square Matrix dimensions */
#define N 1536 


int main( int argc, char **argv )
{
    // Local variables
    int numprocs, rank, rowsPerProc, root=0;
	int i, j;
    double *A=NULL, *b=NULL, *x=NULL, *updated_x=NULL; 
    double start_time=0, end_time=0;

    // Global variables
    int global_i, global_j;
    double *global_A=NULL; 
    double global_errorSumSqrd=0.0;

    // MPI Initialization
	MPI_Init( &argc, &argv );
	MPI_Comm_size( MPI_COMM_WORLD, &numprocs );
	MPI_Comm_rank( MPI_COMM_WORLD, &rank );

    // Memory allocation
    rowsPerProc = N / numprocs;
    A = (double*) malloc( sizeof(double)*N*rowsPerProc );
    b = (double*) malloc( sizeof(double)*N );
    x = (double*) malloc( sizeof(double)*N );
    if(rank == root) { global_A = (double*) malloc( sizeof(double)*N*N ); }

    // Initializing A, x, b on rank 0
    if (rank == root )
    {

        for( i=0; i<N; i++ )
        {
            b[i] = 1.0;									/* Choose a simple vector b */
            x[i] = 0.0;									/* Initial guess for x */
            for( j=0; j<N; j++ )
            {	
                global_A[i*N+j] = 0.0;			        	    /* A[i*N+j] = A[i][j] */ 
                if( i==j ) global_A[i*N+j] = - 2.0;	    		/* Diagonal elements */
                if( i==j+1 || i==j-1 ) global_A[i*N+j] = 1.0;	/* Adjacent to the diagonal */
            }
        }
    }

    // Timer start
    if (rank == root) { start_time = MPI_Wtime(); }

    // Sending relevant A, x, b to each process
    MPI_Scatter(global_A, N*rowsPerProc, MPI_DOUBLE, A, N*rowsPerProc, MPI_DOUBLE, root, MPI_COMM_WORLD);
    MPI_Bcast(x, N, MPI_DOUBLE, root, MPI_COMM_WORLD); 
    MPI_Bcast(b, N, MPI_DOUBLE, root, MPI_COMM_WORLD);

	/*
	   Main iteration loop.
	*/
    //int maxIters = 2000;
	int iters = 0;
	double errorSumSqrd, old_x;
	double convTol = 0.9;							/* Convergence tolerance */

	do
	{
		/* Set the error to zero; will update as we go along */
		errorSumSqrd = 0.0;
		
		/* Loop over 'red' and 'black' rows of A */
		int redBlack;
		for( redBlack=0; redBlack<2; redBlack++ )	/* i.e. 0 for red, 1 for black */
		{
			/* Loop over all red or black rows in the matrix. */
			for( i=0; i<rowsPerProc; i++ )
            {
                global_i = i + rank*rowsPerProc;

				if( i%2 == redBlack )
				{
					/* Calculate the new value of x corresponding to this matrix row */
					double sum = 0.0;
					for( j=0; j<N; j++ )					/* j is the column index */
                    {
                        global_j = j;

						if( global_j != global_i )						/* Loop over all non-diagonal elements */
							sum += A[i*N+global_j] * x[global_j];
                    }
					
					/* Store the old value of x[i], purely for the purposes of calculating the error */
					old_x = x[global_i];
					
					/* Complete the Gauss-Seidel calculation. When doing this in parallel, think carefully about
					   each index in this local system and how it relates to the global system (see Lecture 7). */

					x[global_i] = ( b[global_i] - sum ) / A[i*N + global_i];		/* A[i*N+i]=A[i][i] */ 
					
					/* Update the error; sum of the squares of the change in x[i] */
					errorSumSqrd += ( x[global_i] - old_x )*( x[global_i] - old_x );
				}
            }
		} /* End of 'redBlack' loop, i.e. a single, complete iteration */		

        // Gathers only the updated x values from all ranks to rank 0
        if (rank == root)
        {
            MPI_Gather(MPI_IN_PLACE, rowsPerProc, MPI_DOUBLE, x, rowsPerProc, MPI_DOUBLE, root, MPI_COMM_WORLD); 
        }
        else
        {
            updated_x = x + rank*rowsPerProc;
            MPI_Gather(updated_x, rowsPerProc, MPI_DOUBLE, x+rowsPerProc, N-rowsPerProc, MPI_DOUBLE, root, MPI_COMM_WORLD); 
        }

        // Sending the gathered fully updated x array to all ranks 
        MPI_Bcast(x, N, MPI_DOUBLE, root, MPI_COMM_WORLD);

        // Summing all the errors from all ranks to compute global error
        MPI_Allreduce(&errorSumSqrd, &global_errorSumSqrd, 1, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);

        iters++;

	} while(sqrt(global_errorSumSqrd/N) > convTol);

    // Timer end
    if (rank == root) 
    { 
        end_time = MPI_Wtime(); 
        printf("TIME TAKEN: %f seconds\n", end_time-start_time);
        printf( "Iteration converged after %i iterations; final error was %g.\n", iters, sqrt(global_errorSumSqrd/N) );
    }

    // Check the result (small systems only)
	if( N<50 )
	{
		printf( "\nChecking solution:\n" );
		for( i=0; i<N; i++ )		/* Loop over each row of the matrix */
		{
			double sum = 0.0;
			for( j=0; j<N; j++ )
				sum += A[i*N+j] * x[j];
			printf( "Row %i:\tAx=%g,\tb=%g.\n", i, sum, b[i] );
		}
	}

    // Free memory and exit successfully 
    if(rank == root) { free( global_A ); }
    free( A );
	free( b );
	free( x );
    MPI_Finalize();
	return EXIT_SUCCESS;
}

