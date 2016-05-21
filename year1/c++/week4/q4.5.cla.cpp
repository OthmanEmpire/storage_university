// Demo of command line arguments
// (NDE, 2015-01-05)

#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
  cout << "argc = " << argc << endl;

  for (int i = 0; i < argc; ++i) {
    cout << "argv[" << i << "] = " << argv[i] << endl;
  }

  return 0;
}
