#include <iostream>


int fibonacci2(int n);

int fibonacci(int n)
{
	std::cout << "F1: ";
	if(n == 0 or n == 1)
	{
		std::cout << "1\n";
		return 1;
	}
	else
	{
		std::cout << n << ", ";
		return fibonacci(n - 1) + fibonacci2(n - 2);
	}
}

int fibonacci2(int n)
{
	std::cout << "F2: ";
	if(n == 0 or n == 1)
	{
		std::cout << n << "\n";
		return 1;
	}
	else
	{
		std::cout << n << ", ";
		return fibonacci2(n - 1) + fibonacci2(n - 2);
	}
}

int main()
{
	std::cout << "\nFibonnaci: " << fibonacci(6) << std::endl;
}
