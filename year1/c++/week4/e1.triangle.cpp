#include <iostream>
#include <cmath>


double applyHeroism(double a, double b, double c)
{
	double area;
	double s;

	s = (a + b + c)/2;	// semi-perimeter
	area = 	sqrt(s * (s - a) * (s - b) * (s - c));	// Hero's formula :o

	return area;
}

int main()
{
	double a = 0;
	double b = 0;
	double c = 0;
	double area = 0;

	std::cout << "Welcome to Hero's Realm, version 1.0.0\n"
		  << "Please input the sides of your triangles:\n"
		  << "e.g. 12 13 15\n" << std::endl;
	std::cin >> a >> b >> c;

	area = applyHeroism(a, b, c);

	std::cout << "Area: " << area << std::endl;

}
