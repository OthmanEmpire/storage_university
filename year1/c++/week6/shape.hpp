// A superclass for different types of shape
// (NDE, 2015-02-08)

#pragma once

#include <cmath>   // for hypot function

class Shape
{
  public:
    Shape(int x_, int y_): x(x_), y(y_) {}
    int get_x() const { return x; }
    int get_y() const { return y; }
    double distance() const { return hypot(x, y); }

  protected:
    int x, y;
};
