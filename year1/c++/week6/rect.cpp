// Rectangle as a subclass - implementation file
// (NDE, 2015-02-08)

#include <stdexcept>
#include <iostream>
#include "rect.hpp"

Rectangle::Rectangle(int x, int y, int w, int h): Shape(x, y)
{
  if (w < 1 or h < 1) {
    throw std::invalid_argument("width & height must be >= 1");
  }

  width = w;
  height = h;
}

std::ostream& operator << (std::ostream& out, const Rectangle& rect)
{
	out << "Rectangle: "
      	    << rect.get_width() << "x" << rect.get_height()
       	    << " at (" << rect.get_x() << "," << rect.get_y() << ")";

  return out;
}

std::istream& operator >> (std::istream& in, Rectangle& rect)
{
	in >> rect.x >> rect.y >> rect.width >> rect.height;

	return in;
}
