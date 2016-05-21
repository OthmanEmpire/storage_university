// Test program for a swap function
// (NDE, 2014-12-12)

#include <iostream>

using namespace std;

void swap(int &x, int &y);

int main()
{
  int first, second;

  cout << "Enter first integer: ";
  cin >> first;
  cout << "Enter second integer: ";
  cin >> second;

  cout << "Before swapping: " << first << " " << second << endl;

  swap(first, second);

  cout << "After swapping: " << first << " " << second << endl;

  return 0;
}

void swap(int &x, int &y)
{
	int temp = x;
	x = y;
	y = temp;
}
