#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


void read_data(ifstream& infile, vector<double>& data)
{
  double value;

  while (infile >> value) {
    data.push_back(value);
  }
}
