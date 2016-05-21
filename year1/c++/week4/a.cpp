// Example of a program split into several functions
// (NDE, 2013-01-19)

#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>

using namespace std;


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

