// Example of a class implementation - see also rect.hpp
// (NDE, 2015-01-06)

#include <stdexcept>
#include "rec.hpp"

Rectangle::Rectangle(int x, int y, int w, int h):
	corner_x(x), corner_y(y), width(w), height(h)
{
  if (w < 1 or h < 1) {
    throw std::invalid_argument("width & height must be >= 1");
  }
}

int Rectangle::get_x()
{
  return corner_x;
}

int Rectangle::get_y()
{
  return corner_y;
}

int Rectangle::get_width()
{
  return width;
}

int Rectangle::get_height()
{
  return height;
}

int Rectangle::get_perimeter()
{
	return 2*(width + height);
}

int Rectangle::get_area()
{
	return width*height;
}
