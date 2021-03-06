#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void read_data(ifstream&, vector<double>&);
double mean(const vector<double>&);
double median(vector<double>);

int main(int argc, char* argv[])
{
  // Check command line

  if (argc != 2) {
    cerr << "Error: filename required" << endl;
    return 1;
  }

  // Open file

  ifstream infile(argv[1]);
  if (not infile.is_open()) {
    cerr << "Error: cannot open file" << endl;
    return 1;
  }

  // Populate vector with data

  vector<double> data;
  read_data(infile, data);

  int size = data.size();
  cout << "Vector has " << size << " elements" << endl;

  // Compute mean and median

  cout << "Mean = " << mean(data) << endl;
  cout << "Median = " << median(data) << endl;

  return 0;
}
