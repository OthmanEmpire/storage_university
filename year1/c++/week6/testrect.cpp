#include <iostream>
#include "shape.hpp"
#include "rect.hpp"


int main()
{
	Rectangle rect1(1,1,100,100);

	std::cout << "Area: " << rect1.area() << '\n'
		  << "Hypot: " << rect1.distance() << '\n';

	std::cout << rect1;
}
