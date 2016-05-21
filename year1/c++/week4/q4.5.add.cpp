// Example of using numeric command line arguments
// (NDE, 2015-01-05)

#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
  // Check for correct number of CLAs

  if (argc != 3) {
    cerr << "Usage: " << argv[0] << " <num1> <num2>" << endl;
    return 1;
  }

  // Convert CLAs to numbers

  double num1 = atof(argv[1]);
  double num2 = atof(argv[2]);

  // Add numbers and display the result

  double sum = num1 + num2;

  cout << "Sum = " << sum << endl;

  return 0;
}
