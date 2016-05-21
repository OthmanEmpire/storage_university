// Example of a class definition - see also rect.cpp
// (NDE, 2015-01-06)

class Rectangle
{
  public:
    Rectangle(int, int, int, int);
    int get_x();
    int get_y();
    int get_width();
    int get_height();
    int get_perimeter();
    int get_area(); 

  private:
    int corner_x;
    int corner_y;
    int width;
    int height;
};
