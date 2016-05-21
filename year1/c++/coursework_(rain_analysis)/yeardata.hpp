#include <iostream>
#include <vector>
#include "row.hpp"
#pragma once


// Groups the Rows by years to simplify data manipulation 
class YearData
{
	public:
		YearData() {};

		int getYear() const {return months[0].getYear();}
		Row getRow(int rowNum) const {return months[rowNum];}

		double computeTotalRain() const;
		double computeAverageRain() const;
		void addMonthData(Row row); 

	private:
		std::vector<Row> months;
};

std::ostream& operator << (std::ostream& out, const YearData& year);
