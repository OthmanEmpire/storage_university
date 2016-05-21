/*
	This file contains a serial quicksort routine, and a number of debugging routines
	that display the current state of the algorithm. These are intended to help you
	develop and debug your solution, and it is highly recommended (although not
	compulsory) that you use these routines.
	
	You should not include this file in your coursework submission. For this reason,
	DO NOT MODIFY THESE ROUTINES, as there will be no way of knowing what changes you
	might have made.

	The simplest way to use these routines is just to place this file in your current
	work directory, and insert the line:
	
	#include "routines.c"
	
	near the start of your .c file (this has already been included in the provided
	file coursework.c). You should then be able to compile and execute as normal.
*/


/* Includes */
#include <stdio.h>		/* Needed for printf() */
#include <stdlib.h>		/* Needed for free() and malloc() */
#include <mpi.h>		/* Needed for the debugging routines */
#include <time.h>		/* Used to set the random number seed */


/*
	Serial quicksort in-place. You should call the routine "serialQuicksort()" (below) as:
	
	serialQuickSort( list, start, end );
	
	with
	
	float *list;			List to be sorted
	int start;				Start index (initially 0; becomes non-zero during recursion)
	int end;				End index (i.e. the list size if start=0).

*/	
int serialPartition( float *list, int start, int end, int pivotIndex )
{
	/* Scratch variables */
	float temp;

	/* Get the pivot value */
	float pivotValue = list[pivotIndex];

	/* Move pivot to the end of the list (or list segment); swap with the value already there. */
	list[pivotIndex] = list[end-1];
	list[end-1]      = pivotValue;

	/* Sort into sublists using swaps; get all values below the pivot to the start of the list */
	int storeIndex = start, i;					/* storeIndex is where the values less than the pivot go */
	for( i=start; i<end-1; i++ )		/* Don't loop over the pivot (currently at end-1); will handle that just before returning */
		if( list[i] <= pivotValue )
		{
			/* Swap value with this element and that at the current storeIndex */
			temp = list[i]; list[i] = list[storeIndex]; list[storeIndex] = temp;

			/* Increment the store index; will point to one past the pivot index at the end of this loop */
		storeIndex++;			/* Could do this at the end of the previous instruction */
	}

	/* Move pivot to its final place */
	temp = list[storeIndex]; list[storeIndex] = list[end-1]; list[end-1] = temp;

	return storeIndex;
}

/* Performs the quicksort (partitioning and recursion) */
void serialQuicksort( float *list, int start, int end )
{
	if( end > start+1 )
	{
		int pivotIndex = start;				/* Choice of pivot index */

		/* Partition and return list of pivot point */
		int finalPivotIndex = serialPartition( list, start, end, pivotIndex );

		/* Recursion on sublist smaller than the pivot (including the pivot value itself) ... */
		serialQuicksort( list, start, finalPivotIndex );

		/* .. and greater than the pivot value (not including the pivot) */
		serialQuicksort( list, finalPivotIndex+1, end );
	}
	/* else ... only had one element anyway; no need to do anything */
}


/*
	DEBUGGING ROUTINES: Print current state of the algorithm from rank 0.
*/

/*
	Display the full list, assumed to be on rank==0 only (although it is safe to call
	this routine from all ranks). Call as:
	
	displayFullList( list, rank, numprocs, n );
	
	where
	
	float *list;				The list of numbers (defined on rank 0)
	int rank;					Rank of this process
	int numprocs;				Total number of processes
	int n;						List size
	
	Will not attempt to display large lists.

*/
void displayFullList( float *list, int rank, int numprocs, int n )
{
	if( rank != 0 ) return;

	/* Do not display large lists */
	if( n>100 )
	{
		printf( "Not displaying 'full list' - n too large.\n" );
		return;
	}

	printf( "\nFull list:" );
	
	int i;
	for( i=0; i<n; i++ ) printf( " %g", list[i] );
	printf( "\n" );
}


/*
	Display state of bigBucket arrays. Call (from each rank) as:
	
	displayBigBuckets( bigBuckets, size, rank, numprocs, n );
	
	where:
	
	float *bigBuckets;			Array of numbers in this rank's 'big bucket'
	int size;					Number of entries in this rank's 'big bucket'
	int rank;					Rank of this process
	int numprocs;				Total number of processes
	int n;						Total list size
	
	Note that large lists are not printed. Uses MPI_Get_count() to determine the message
	size after it is sent.

*/
void displayBigBuckets( float *bigBucket, int size, int rank, int numprocs, int n )
{
	if( n>100 )
	{
		if( rank==0 ) printf( "Not displaying 'big buckets' - n too large.\n" );
		 return;		/* Not large lists */
	}

	/* If not on rank 0, send data to rank==0 display; then we are done (rank 0 does most of the work) */
	if( rank != 0 )
		MPI_Send( bigBucket, size, MPI_FLOAT, 0, 0, MPI_COMM_WORLD );
	
	/* Rank 0 displays its own bigBucket, and displays that of all other processes
	   as it receives them in order. */
	if( rank==0 )
	{
		int i, p;
		MPI_Status status;

		/* Array for temporary storage of the data passed by another rank */
		float *scratchArray = (float*) malloc( sizeof(float)*n );

		/* Print message header, and contents of rank 0's bigBucket */
		printf( "\nCurrent state of big buckets.\n" );
		printf( "Rank 0:" );
		for( i=0; i<size; i++ ) printf( " %g", bigBucket[i] );
		printf( "\n" );
		
		/* Print contents of each other rank's big bucket as they ar received */
		for( p=1; p<numprocs; p++ )
		{
			int scratchSize;
			MPI_Recv( scratchArray, n, MPI_FLOAT, p, 0, MPI_COMM_WORLD, &status );	/* Maximum count is n */
			MPI_Get_count( &status, MPI_FLOAT, &scratchSize );
			
			printf( "Rank %i:", p );
			for( i=0; i<scratchSize; i++ ) printf( " %g", scratchArray[i] );
			printf( "\n" );
		}
		
		/* Free up memory */
		free( scratchArray );
	}
}


/*
	Display state of the 2D smallBucket arrays. Call as
	
	displaySmallBuckets( buckets, sizes, rank, numprocs, n );

	where
	
	float **buckets;			2D array ("array of arrays"), first index is small bucket number (ranges 0 to numprocs-1 inc),
								second is the index of the entry within that bucket.
	int *size;					The sizes of each of the small buckets (index range 0 to numprocs-1 inc)
	int rank;					Rank of this process
	int numprocs;				Total number of processes
	int n;						Total list size

	If you are unsure about 2D arrays in C, check Worksheet 1 Question 2.
	
	Will not attempt to display large lists. Uses MPI_Get_count() to determine the message
	size after it is received.
*/
void displaySmallBuckets( float **smallBuckets, int *size, int rank, int numprocs, int n )
{
	int i, p, p2;

	if( n>100 )
	{
		if( rank==0 ) printf( "Not displaying 'small buckets' - n too large.\n" );
		return;
	}

	/* If not on rank 0, send data to rank==0 display */
	if( rank != 0 )
		for( p=0; p<numprocs; p++ )
			MPI_Send( smallBuckets[p], size[p], MPI_FLOAT, 0, 0, MPI_COMM_WORLD );

	/* Rank 0 displays its own small buckets, and displays that of all other processes
	   as it receives them in order. */
	if( rank==0 )
	{
		MPI_Status status;

		/* Array for temporary storage of the data passed by another rank; also its size */
		float *scratchArray = (float*) malloc( sizeof(float)*n );

		/* Print message header, and contents of rank 0's bigBucket */
		printf( "\n\nCurrent state of small buckets.\n" );
		printf( "\nRank 0:\n" );
		for( p=0; p<numprocs; p++ )
		{
			printf( "Small bucket %i:", p );
			for( i=0; i<size[p]; i++ ) printf( " %g", smallBuckets[p][i] );
			printf( "\n" );
		}
		
		/* Print contents of each other rank's big bucket as they ar received */
		for( p=1; p<numprocs; p++ )				/* Outer loop: Rank that sent its smallBuckets */
		{
			printf( "\nRank %i:\n", p );
			for( p2=0; p2<numprocs; p2++ )		/* Inner loop: The small bucket for rank p */
			{
				/* The 'count' argument here is the maximum message size; the worst-case scenario is n */
				MPI_Recv( scratchArray, n, MPI_FLOAT, p, 0, MPI_COMM_WORLD, &status );
				
				/* Now get the actual message size */
				int listSize;
				MPI_Get_count( &status, MPI_FLOAT, &listSize );
			
				printf( "Small bucket %i:", p2 );
				for( i=0; i<listSize; i++ ) printf( " %g", scratchArray[i] );
				printf( "\n" );
			}
		}
		
		/* Free up memory */
		free( scratchArray );
	}
}


/*
	Other routines
*/

/*
	This parses the command line arguments and returns the problem size.
*/
int getProblemSize( int argc, char **argv, int rank, int numprocs )
{
	int n;

	/* Get n from the command line. Note that you should always finalise MPI before quitting. */
	if( argc != 2 )
	{
		if( rank==0 ) printf( "Need one argument (= the list size n).\n" );
		return -1;
	}
	n = atoi( argv[1] );
	if( n<=0 )
	{
		if( rank==0 ) printf( "List size must be >0.\n" );
		return -1;
	}
	
	/* Check n divisible by p, bail if not (with message) */
	if( n%numprocs != 0 )
	{
		if( rank==0 ) printf( "Must have problem size '%i' divisible by the number of processes '%i'\n", n, numprocs );
		return -1;
	}
	
	return n;
}


/*
	Initialise the random list, including the memory allocation for the array (which will
	need to be free()'ed elsewhere).
*/
float* initialiseRandomList( int n )
{
	srand( time(NULL) );		/* Seed the random number generator to the system time */
	float *array = (float*) malloc( sizeof(float)*n );
		
	int i;
	for( i=0; i<n; i++ ) array[i] = 1.0*rand() / RAND_MAX;
	
	return array;
}
