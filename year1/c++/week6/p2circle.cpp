#include <iostream>
#include <stdexcept>
#include "P1Circle.hpp"

Circle::Circle(): Shape(0.0, 0.0), radius(1.0) {};

Circle::Circle(double r, double X, double Y):
	Shape(X, Y), radius(r)
{
	if(r < 0.0 or X < 0.0 or Y < 0.0)
	{
		throw std::invalid_argument("Negative dimensions are not supported");
	}
};

std::ostream& operator << (std::ostream& out, const Circle& circ1)
{
	out << "Radius: " << circ1.getRadius() << '\n'
	    << "CenterX: " << circ1.get_x() << '\n'
	    << "CenterY: " << circ1.get_y() << std::endl;

	return out;
}

bool operator < (const Circle& circ1, const Circle& circ2)
{
	return circ1.getRadius() < circ2.getRadius();
}
