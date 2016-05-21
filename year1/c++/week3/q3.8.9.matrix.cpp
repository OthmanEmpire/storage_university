#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iomanip>


typedef std::vector<double> row; // CHANGE

std::vector<row> matrixMultiplication(std::vector<row> A, std::vector<row> B)
{
	const int ROWA = A.size();
	const int ROWB = B.size();
	const int COLA = A[0].size();
	const int COLB = B[0].size();
	std::vector<row> C(ROWA, row(COLB, 0));

	if(COLA != ROWB)
	{
		throw "ERROR: Matrices cannot be multiplied due to"  
		      "incompatible dimensions !";
	}

	for(int j = 0; j < ROWA; ++j)
	{
		for(int i = 0; i < COLB; ++i)
		{
			for(int k = 0; k < COLA; ++k) // Note: COLA = ROWB
			{
				C[j][i] = C[j][i] + (A[j][k] * B[k][i]);
			}
		}
	}

	return C;
}

void printMatrix2D(std::vector<row> A)
{
	for(unsigned int i = 0; i < A.size(); ++i)
	{	
		std::cout << std::endl;
		for(unsigned int j = 0; j < A[0].size(); ++j)
		{
			std::cout << std::setw(3) << A[i][j] << " ";
		}
	}
	std::cout << std::endl;
}	

std::vector<row> initializeMatrix(std::vector<row> A)
{
	srand(time(NULL));

	for(unsigned int i = 0; i < A.size(); ++i)
	{	
		for(unsigned int j = 0; j < A[0].size(); ++j)
		{
			A[i][j] = rand() % 10;
		}
	}

	return A;
}

int main()
{
	std::vector<row> A(10, row(5));
	std::vector<row> B(5, row(5));	
	std::vector<row> C;

	A = initializeMatrix(A);
	B = initializeMatrix(B);

	try
	{
		C = matrixMultiplication(A, B);
	}
	catch(const char* msg)
	{
		std::cerr << msg << std::endl;
	}
	
	printMatrix2D(A);
	printMatrix2D(B);
	printMatrix2D(C);	
}
