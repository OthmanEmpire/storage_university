#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include "yeardata.hpp"
#include "row.hpp"
#include "gnuplot_i.hpp"


// Opens a file, reads from it, then extracts row contents and stores it in a row object which is then stored into a YearData object which is then stored into a vector, and then returns the vector.
std::vector<YearData> readFile(std::string fileName)
{
	std::ifstream inFile;
	std::string header;
	const int SKIPLINES = 4;	
	
	int year, month;
	double tMax, tMin, airFrostDays, rain, sun;
	std::vector<Row> allRows;
	std::vector<YearData> dataVec;
	YearData yearData;
	
 	// Opening the file

 	inFile.open(fileName.c_str());

 	if(not inFile)
 	{
 		std::cerr << "ERROR: Could not open file! " << std::endl;
 		return dataVec;
 	}

	// Skips over header lines

	for(int i = 0; i < SKIPLINES; ++i)
	{
		getline(inFile, header);
	}

	// Reads the contents of the file and stores the data into a vector 

	while(true)
	{
		YearData yearData;	// Instantiates new variable each loop 

		while(inFile >> year >> month >> tMax >> tMin 
		     >> airFrostDays >> rain >> sun)
		{
			yearData.addMonthData(Row(year, month, tMax, tMin, 
						airFrostDays, rain, sun));

			if(month == 12)
			{
				break;
			}
		}	

		if(not inFile.eof())
		{
			dataVec.push_back(yearData);
		}
		else
		{
			break;
		}
	}

	return dataVec;
}

// Uses a single for-loop over the data structure and hence is of class O(n) 
YearData findWettestYear(std::vector<YearData>& dataVec)
{
	double maxRain = dataVec[0].computeTotalRain();
	YearData maxYear;
	
	for(unsigned int i = 0; i < dataVec.size(); ++i)
	{
		if(maxRain < dataVec[i].computeTotalRain())
		{
			maxRain = dataVec[i].computeTotalRain();
			maxYear = dataVec[i];
		}	
	}

	return maxYear;
}

// Uses a single for-loop over the data structure and hence is of class O(n)
YearData findDriestYear(std::vector<YearData>& dataVec)
{
	double minRain = dataVec[0].computeTotalRain();
	YearData minYear;

	for(unsigned int i = 0; i < dataVec.size(); ++i)
	{
		if(minRain > dataVec[i].computeTotalRain())
		{
			minRain = dataVec[i].computeTotalRain();
			minYear = dataVec[i];
		}	
	}

	return minYear;
}

// Finds the month that produced the most amount of Frosties. (Delicious :o) 
Row findFrostiesMonth(std::vector<YearData>& dataVec)
{
	int maxFrost = dataVec[0].getRow(0).getAirFrost();
	Row maxRow;

	for(unsigned int i = 0; i < dataVec.size(); ++i)
	{
		for(unsigned int j = 0; j < 12; ++j)
		{
			if(maxFrost < dataVec[i].getRow(j).getAirFrost())
			{
				maxFrost = dataVec[i].getRow(j).getAirFrost();
				maxRow = dataVec[i].getRow(j);
			}	
		}
	}
	return maxRow;
}

// Draws a bar chart of the average rainfall per month using GNU plot 
int plotAverageRainPerMonth(std::vector<YearData>& dataVec)
{
	std::vector<double> avgRainData(12,0);
	std::vector<int> timeMonthData(12);

	// Sums up the total rain fallen per month across all the years

	for(unsigned int i = 0; i < dataVec.size(); ++i)
	{
		for(unsigned int j = 0; j < 12; ++j)
		{
			avgRainData[j] += dataVec[i].getRow(j).getRain();
		}
	}

	// Averages out the total rain fallen per month and also generates
	// the corresponding list of months

	for(unsigned int i = 0; i < 12; ++i)
	{
		avgRainData[i] = avgRainData[i]/dataVec.size();
		timeMonthData[i] = i + 1;
	}

	// Plots avgRainData (y-axis) against timeYearData (x-axis)

	try
	{
		Gnuplot g1;

		g1.set_xlabel("Time / Years");
		g1.set_ylabel("Average Rain / mm");
		g1.set_style("boxes").set_pointsize(1);
		g1.set_grid();
		g1.plot_xy(timeMonthData, avgRainData);

		std::cout << "Press ENTER ONLY to continue!";
		std::cin.get();		

		return 0;
	}
	catch (const GnuplotException& err)
	{
		std::cerr << err.what() << std::endl;
		return 1;
	}
}

// Draws a line plot of the maximum temperature as a function of time 
// using GNU plot
int plotMaxTempPerMonth(std::vector<YearData>& dataVec)
{
	std::vector<double> maxTempData, timeLineData;

	// Collects the data of maxTemp & timeLineData (in months) from dataVec

	for(unsigned int i = 0; i < dataVec.size(); ++i)
	{
		for(unsigned int j = 0; j < 12; ++j)
		{
			maxTempData.push_back(
					dataVec[i].getRow(j).getMaxTemp());
			timeLineData.push_back(12*i + j);
		}
	}

	// Plots maxTempData (y-axis) against timeLineData (x-axis)

	try
	{
		Gnuplot g1;

		g1.set_xlabel("Time / Months");
		g1.set_ylabel("Max Temperature / C");
		g1.set_style("lines").set_pointsize(1);
		g1.set_grid();
		g1.plot_xy(timeLineData, maxTempData);

		std::cout << "Press ENTER ONLY to continue!";
		std::cin.get();		

		return 0;
	}
	catch (const GnuplotException& err)
	{
		std::cerr << err.what() << std::endl;
		return 1;
	}
}

// Draws a scatter plot of the maximum temperature against the hours of
// sunshine on GNU plot
int plotMaxTempAgainstSunshine(std::vector<YearData>& dataVec)
{
	std::vector<double> maxTempData, sunData;

	// Collects the data of maxTemp & Sunshine from dataVec 

	for(unsigned int i = 0; i < dataVec.size(); ++i)
	{
		for(unsigned int j = 0; j < 12; ++j)
		{
			maxTempData.push_back(
					dataVec[i].getRow(j).getMaxTemp());
			sunData.push_back(dataVec[i].getRow(j).getSun());
		}
	}	
	
	// Plots maxTempData (y-axis) against sunData (x-axis)

	try
	{
		Gnuplot g1;
	
		g1.set_xlabel("Sunshine / hrs");
		g1.set_ylabel("Max Temperature / C");
		g1.set_style("points").set_pointsize(1).set_grid();
		g1.plot_xy(sunData, maxTempData);
	
		std::cout << "Press ENTER ONLY to continue!";
		std::cin.get();		

		return 0;
	}
	catch (const GnuplotException& err)
	{
		std::cerr << err.what() << std::endl;
		return 1;
	}
}

int main(int argc, char** argv)
{
	std::string fileName;
	std::vector<YearData> dataVec;

	// Checks whether only a single file has been inputted in command line
	
	if(argc != 2)
	{
	 	std::cerr << "ERROR: Can only accept a SINGLE file! " 
	 		  << std::endl;
	 	return 1;
	}

	fileName = argv[1];

	// Extracts data from file and does some error checking

	dataVec = readFile(fileName);
	if(dataVec.empty())
	{
		return 0;
	}

	std::cout << "\n\nWelcome to Analyze, version 1.0.1, the "
			"unanalyzed version!\n" << std::endl;

	std::cout << "\nWettest year corresponds to the following row:\n\n" 
		  << findWettestYear(dataVec) << std::endl;

	std::cout << "Driest year corresponds to the following row:\n\n" 
		  << findDriestYear(dataVec) << std::endl;

	std::cout << "Frosties month corresponds to the following row:\n\n"
		  << findFrostiesMonth(dataVec) << std::endl;

	plotAverageRainPerMonth(dataVec);
	plotMaxTempPerMonth(dataVec);
	plotMaxTempAgainstSunshine(dataVec);
}
