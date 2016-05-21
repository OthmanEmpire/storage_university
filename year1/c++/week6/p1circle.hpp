#include <cmath>
#include <iostream>
#include "shape.hpp"

#pragma once

class Circle: public Shape
{
	public:
		Circle();
		Circle(double radius, double centerX, double centerY);
		double getRadius() const { return radius; }
		double getPerimeter() const { return 2 * M_PI * radius; }
		double getArea() const { return M_PI * pow(radius, 2); }

	private:
		double radius;
};

std::ostream& operator << (std::ostream&, const Circle&);
bool operator < (const Circle&, const Circle&);
