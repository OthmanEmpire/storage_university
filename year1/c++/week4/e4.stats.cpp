// Example of a program split into several functions
// (NDE, 2013-01-19)

#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <time.h>
#include <cstdlib>
#include <iterator>
#include <math.h>


using namespace std;

void write_data(ofstream& outfile)
{
	srand(time(NULL));

	for(int i = 0; i < 10; ++i)
	{
		outfile << rand()%10 << " ";
	}

	outfile.close();
}
	

void read_data(ifstream& infile, vector<double>& data)
{
  double value;


  while (infile >> value) {
    data.push_back(value);
  }
}


double mean(const vector<double>& data)
{
  double sum = accumulate(data.begin(), data.end(), 0.0);

  return sum / data.size();
}


double median(vector<double> data)
{
  // Note that 'data' is not a reference; we deliberately allow
  // copying to take place here because computation of the median
  // involves sorting the values, and it might be important to
  // preserve the order of values in the vector that is used as an
  // argument to this function

  sort(data.begin(), data.end());

  int middle = data.size() / 2;

  if (data.size() % 2 == 0) {
    // Even number of elements, so no unique middle
    return 0.5*(data[middle] + data[middle-1]);
  }
  else {
    return data[middle];
  }
}


double standardDeviation(const vector<double>& data, double mean)
{
	double calc1 = 0;
	double standardDeviation = 0;
	double size = data.size();

	for(int i = 0; i < size; ++i)
	{
		calc1 = calc1 + pow((data[i] - mean), 2);
	}

	standardDeviation = sqrt(calc1 / size);

	return standardDeviation;
}

int main(int argc, char* argv[])
{
  // Check command line

  if (argc != 2) {
    cerr << "Error: filename required" << endl;
    return 1;
  }

  // Open file to write data
  
  ofstream outfile(argv[1]);
  if (not outfile)
  {
    cerr << "Error: cannot open file! " << endl;
    return 1;
  }

  write_data(outfile);

  // Open file to read data

  ifstream infile(argv[1]);
  if (not infile.is_open()) {
    cerr << "Error: cannot open file" << endl;
    return 1;
  }

  // Populate vector with data

  vector<double> data;
  ostream_iterator<double> out(cout, " ");
  read_data(infile, data);

  int size = data.size();
  cout << "Vector has " << size << " elements" << endl;
  copy(data.begin(), data.end(), out);
  cout << endl;

  // Compute mean and median

  cout << "Mean = " << mean(data) << endl;
  cout << "Median = " << median(data) << endl;
  cout << "Standard Deviation = " << standardDeviation(data, mean(data)) 
	  			  << endl;

  return 0;
}
