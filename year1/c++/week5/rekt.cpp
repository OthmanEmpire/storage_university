#include <iostream>
#include "rect.cpp"

int main()
{
	Rectangle rect(10,10,20,30);

	std::cout << "Width: " << rect.get_width() 
		  << "\nHeight: " << rect.get_height() 
		  << "\nPerimeter: " << rect.get_perimeter()
		  << " \nArea: " << rect.get_area();
}
