#include <iostream>
#include "E1Circle.hpp"


int main()
{
	double r, X, Y;
	Circle circ2;

	std::cout << "Please enter your coordinates:" << std::endl;
	
	std::cout << "X: ";
	std::cin >> X;

	std::cout << "Y: ";
	std::cin >> Y;

	std::cout << "Radius: ";
	std::cin >> r;
	std::cout << std::endl;

	try: 
	{ 
		Circle circ1(r, X, Y); 
	}
	catch(const std::invalid_argument& ia) 
	{ 
		std::cerr << "Invalid argument: " << ia.what() << std::endl;
		return -1;
	}
	
	std::cout << "CIRCLE1" << '\n' 
		  << circ1 << '\n'
		  << "Area: " << circ1.getArea() << '\n'
		  << "Perimeter: " << circ1.getPerimeter() << '\n' << std::endl;

	std::cout << "Circle1 radius: " << circ1.getRadius() << '\n'
		  << "Circle2 radius: " << circ2.getRadius() << '\n'
		  << "Circle1 < Circle2: " << std::boolalpha 
		  <<  (circ1 < circ2) << std::endl;
}
