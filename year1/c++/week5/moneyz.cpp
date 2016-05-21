#include <iostream>
#include "moneys.cpp"
#include <sstream>

int main()
{
	Money A;
	const Money B(50,1);
	Money sum;

	sum = A + B;
	std::cout << sum;

	std::cout << std::boolalpha << (A < B) << std::endl;

}
