// Rectangle as a subclass - definition
// (NDE, 2015-02-08)

#pragma once

#include <iostream>
#include "shape.hpp"

class Rectangle: public Shape
{
  friend std::istream& operator >> (std::istream&, Rectangle&);
  
  public:
    Rectangle(int, int, int, int);
    int get_width() const { return width; }
    int get_height() const { return height; }
    int perimeter() const { return 2*(width+height); }
    int area() const { return width*height; }

  private:
    int width;
    int height;
};

std::ostream& operator << (std::ostream&, const Rectangle&);
