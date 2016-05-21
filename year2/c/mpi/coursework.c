/*
    Parallel implementation of Bucket Sort.
*/


#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#include "routines.c"


int main(int argc, char **argv)
{	
    /* Variable declaration */
    float 
        *globalArray = NULL,
        *bBucket = NULL,
        **sBucket = NULL,
        *tempArray = NULL,
        value;

    int 
	    dataPerProc, numprocs, rank, i, p, n,
        size, maxTempSize, assignedIndex,
         bSize, bMaxSize, bTotal,
        *sSize, sMaxSize, sTotal, sAssigned;
        
    MPI_Status status, recvStatus;
    MPI_Request sendRequest, recvRequest;

    /* Initliaze MPI */
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank    );

    /* Initializing from CL arguments */
	n = getProblemSize(argc, argv, rank, numprocs);
	if(n==-1)
	{
		MPI_Finalize();
		return EXIT_FAILURE;
	}
    else
    {
        dataPerProc = n/numprocs;
        maxTempSize = n;

        bMaxSize = n;
        sMaxSize = dataPerProc;

        bTotal = numprocs;
        sTotal = numprocs;
    }

    /* Initializing buckets and arrays */
	if(rank==0) globalArray = initialiseRandomList(n);
    tempArray = (float*) malloc(sizeof(float)*maxTempSize);

    bBucket = (float*) malloc(sizeof(float)*bMaxSize);
	sBucket = (float**) malloc(sizeof(float*)*sTotal);
	for(i=0; i<sTotal; i++) sBucket[i] = (float*) malloc(sizeof(float)*sMaxSize);

    bSize = dataPerProc;
    sSize = (int*) calloc(numprocs, sizeof(int));


    /* Start timer */
	double startTime = MPI_Wtime();
	if( rank==0 ) printf( "Starting iteration; may take a few seconds ...\n" );


    /* Scatter global array into big buckets */
	displayFullList(globalArray, rank, numprocs, n);
    MPI_Scatter(globalArray, dataPerProc, MPI_FLOAT, bBucket, dataPerProc, MPI_FLOAT, 0, MPI_COMM_WORLD); 
    displayBigBuckets(bBucket, bSize, rank, numprocs, n);


    /* Pour each rank's big buckets into the correct small bucket */
    /* Step 1 to Step 2 of Lecture 8 */
    for(i=0; i<dataPerProc; i++)
    {
        value = bBucket[i];

        sAssigned = (int) (value * numprocs);
        if(sAssigned == numprocs) sAssigned--;  /* Resolves a bug cropping due to numerical errors;
                                                 * e.g. int(0.99 * 1) = 1 but first bucket is index 0*/
        assignedIndex = sSize[sAssigned];
        sBucket[sAssigned][assignedIndex] = value;
        sSize[sAssigned] += 1;
    }
//    for(i=0; i<sTotal; i++) printf("\nRank %i: sBucket=%i, Size=%i\n", rank, i, sSize[i]);
    displaySmallBuckets(sBucket, sSize, rank, numprocs, n);


    /* Pour each rank's small bucket back into the correct big bucket 
     * The use of non-blocking communication to prevent deadlock when
     * problem size is rather large (although there exists a way solution
     * that doesn't involve non-blocking communication)*/
    /* Step 2 to Step 3 of Lecture 8 */
    for(i=0; i<bMaxSize; i++) bBucket[i] = 0.0;
    bSize = 0;

    for(p=0; p<sTotal; p++)
    {   
        if(p==rank)
        { 
            for(i=0; i<sSize[p]; i++) 
                bBucket[bSize + i] = sBucket[p][i];
                bSize += sSize[p];
        }
        else
        {
            MPI_Isend(sBucket[p], sSize[p], MPI_FLOAT, p, 0, MPI_COMM_WORLD, &sendRequest);

            MPI_Irecv(tempArray, maxTempSize, MPI_FLOAT, p, 0, MPI_COMM_WORLD, &recvRequest);
            MPI_Wait(&recvRequest, &recvStatus);
            MPI_Get_count(&recvStatus, MPI_FLOAT, &size);

            for(i=0; i<size; i++) bBucket[bSize + i] = tempArray[i];
            bSize += size;
        }
    }
    /* All small buckets should pour their entire contents into the big buckets 
     * before just before serial sorting of big buckets */
    MPI_Barrier(MPI_COMM_WORLD);
    displayBigBuckets(bBucket, bSize, rank, numprocs, n);


    /* Swirl each rank's big bucket until sorted */
    /* Step 3 to Step 4 of Lecture 8 */
    serialQuicksort(bBucket, 0, bSize);
    displayBigBuckets(bBucket, bSize, rank, numprocs, n);
    

    /* Concatenate each rank's big bucket */
    /* Step 4 to Step 5 of Lecture 8 */
    if(rank!=0) MPI_Send(bBucket, bSize, MPI_FLOAT, 0, 0, MPI_COMM_WORLD);
    else
    {
        for(p=1; p<bTotal; p++)
        {
            MPI_Recv(tempArray, maxTempSize, MPI_FLOAT, p, 0, MPI_COMM_WORLD, &status);
            MPI_Get_count(&status, MPI_FLOAT, &size);

            for(i=0; i<size; i++) bBucket[bSize + i] = tempArray[i];
            bSize += size;
        }
        globalArray = bBucket;
    }


    /* End timer */
	double timeTaken = MPI_Wtime() - startTime;
	if( rank==0 ) 
    {
        printf( "Finished. Time taken: %g seconds\n", timeTaken );

//        FILE *f = fopen("data.txt", "a");
//        fprintf(f, "%g\n", timeTaken); 
    }

	/*
		Display the final (hopefully sorted) list, and check all entries are indeed in order.
	*/
	displayFullList(globalArray,rank,numprocs,n);			/* Again, nothing is displayed if n>100. */
	if(rank==0)
	{
		for(i=0; i<n-1; i++)
			if(globalArray[i] > globalArray[i+1])
			{
				printf("List not sorted correctly.\n");
				break;
			}
		if(i==n-1) printf("List correctly sorted.\n");
	}


	/*
		Clear up and quit. As ever, each malloc() needs a free().
	*/
    free(bBucket);  // Also frees global array
    for(i=0; i<sTotal; i++) free(sBucket[i]);
    free(sBucket);

    free(sSize);
    free(tempArray);

	MPI_Finalize();
	return EXIT_SUCCESS;
}
