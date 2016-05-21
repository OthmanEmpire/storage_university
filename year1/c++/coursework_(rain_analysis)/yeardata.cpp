#include <iostream>
#include "yeardata.hpp"

// Pushes back a row object (which is essentially a month along with information about that month) into the months private field
void YearData::addMonthData(Row row)
{
	months.push_back(row);
}

// Sums up all the rain values fallen in the 12 months via for-loop.
double YearData::computeTotalRain() const
{
	double totalRain = 0.0;

	for(int i = 0; i < 12; ++i)
	{
		totalRain += months[i].getRain();
	}	

	return totalRain;
}

// Averages out the rain per month by summing up all the rain values then
// dividing by 12
double YearData::computeAverageRain() const
{
	return YearData::computeTotalRain()/12;
}

// Prints out the year along with the total rainfall that year
std::ostream& operator << (std::ostream& out, const YearData& year)
{
	out << "Year: " << year.getYear() << "\n"
	    << "Total rainfall: " << year.computeTotalRain() << "\n"
	    << std::endl;

	return out;
}
