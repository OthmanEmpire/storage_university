#include <iostream>
#pragma once

// A class for storing a row from the "sheffield.data" file.
class Row
{
	public:

		Row();

		Row(const int year,
		    const int month,
		    const double maxTemp,
		    const double minTemp,
		    const int airFrost,
		    const double rain,
		    const double sun);
		
		int getYear() const {return year;}
		int getMonth() const {return month;}
		double getMaxTemp() const {return maxTemp;}
		double getMinTemp() const {return minTemp;}
		int getAirFrost() const {return airFrost;}
		double getRain() const {return rain;}
		double getSun() const {return sun;}

		std::string getStringMonth() const;

	private:
		int year;
		int month;
		double maxTemp;
		double minTemp;
		int airFrost;
		double rain;
		double sun;
};

std::ostream& operator << (std::ostream& out, const Row& row);
