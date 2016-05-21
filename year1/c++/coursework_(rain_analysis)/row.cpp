// The class is used to allow ease of data manipulation extracted from the "sheffield.txt" file.

#include <map>
#include "row.hpp"

Row::Row() {};

Row::Row(const int year,
         const int month,
         const double maxTemp,
         const double minTemp,
	 const int airFrost,
     	 const double rain,
	 const double sun):
	year(year), month(month), maxTemp(maxTemp), minTemp(minTemp),
	airFrost(airFrost), rain(rain), sun(sun) {}

// Converts the month from into to string (e.g. 1 --> January)
std::string Row::getStringMonth() const
{
	std::map<int,std::string> monthMap;
	int month = this->getMonth();

	monthMap[1] = "Jan";
	monthMap[2] = "Feb";
	monthMap[3] = "Mar";
	monthMap[4] = "Apr";
	monthMap[5] = "May";
	monthMap[6] = "Jun";
	monthMap[7] = "Jul";
	monthMap[8] = "Aug";
	monthMap[9] = "Sep";
	monthMap[10] = "Oct";
	monthMap[11] = "Nov";
	monthMap[12] = "Dec";

	return monthMap[month];
}

std::ostream& operator << (std::ostream& out, const Row& row)
{
	out << "Year: " << row.getYear() << "\n"
	    << "Month: " << row.getStringMonth() << "\n"
	    << "MaxTemp: " << row.getMaxTemp() << "C\n"
	    << "MinTemp: " << row.getMinTemp() << "C\n"
	    << "AirFrost: " << row.getAirFrost() << "\n"
	    << "Rain: " << row.getRain() << "mm\n"
	    << "Sun: " << row.getSun() << " hrs\n"
	    << std::endl;

	return out;
}	
