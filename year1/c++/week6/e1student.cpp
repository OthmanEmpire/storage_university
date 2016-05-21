// Represents the abilities a that the character does in the story book

# pragma once

#include <iostream>
#include <string>
#include "E1Student.hpp"


Student::Student(std::string name_, 
		std::string degree_, 
		int year_,
		std::string rank_,
		std::string symbol_, 
		std::string colour_, 
		int executionDate_):

	name(name_), 
	degree(degree_), 
	year(year_), 
	rank(rank_),
	symbol(symbol_), 
	colour(colour_), 
	executionDate(executionDate_) 
	{}

std::ostream& operator << (std::ostream& out, Student people1)
{
	out << "ATTENDANCE REGISTER:" << "\n";

	out << "Name: " << people1.getName() << "\n"
	    << "Degree: " << people1.getDegree() << "\n"
	    << "Year: " << people1.getYear() << "\n"
	    << "Rank: " << people1.getRank() << " of "
	    << people1.getSymbol() <<  "\n"
	    << "Colour: " << people1.getColour() << "\n"
	    << "Execution Date: " << people1.getExecutionDate() << "\n";

	return out;
}	

