// Represents a character in the story book

# pragma once

#include <iostream>
#include <string>


class Student
{
	public:
		Student(std::string name, 
			std::string degree, 
			int year,
			std::string rank,
			std::string symbol, 
			std::string colour, 
			int executionDate);

		std::string getName() const {return name;}
		std::string getDegree() const {return degree;}
		int getYear() const {return year;}
		
		std::string getRank() const {return rank;}
		std::string getSymbol() const {return symbol;}
		std::string getColour() const {return colour;}
		int getExecutionDate() const {return executionDate;}

	private:
		std::string name;
		std::string degree;
		int year;

		std::string rank;
		std::string symbol;
		std::string colour;
		int executionDate;
};

std::ostream& operator << (std::ostream& out, Student people1);
