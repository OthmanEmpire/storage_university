#include <cmath>
#include <iostream>
#pragma once

class Circle
{
	public:
		Circle();
		Circle(double radius, double centerX, double centerY);
		double getX() const { return centerX; }
		double getY() const { return centerY; }
		double getRadius() const { return radius; }
		double getPerimeter() const { return 2 * M_PI * radius; }
		double getArea() const { return M_PI * pow(radius, 2); }

	private:
		double centerY;
		double centerX;
		double radius;
};

std::ostream& operator << (std::ostream&, const Circle&);
bool operator < (const Circle&, const Circle&);
