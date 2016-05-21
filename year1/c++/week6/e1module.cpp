// The actions and events of the party

#include <iostream>
#include "E1Student.hpp"
#include "E1Module.hpp"


void Module::enrolStudent(Student people1)
{
	students.push_back(people1);
}

void Module:: printAttendanceRegister()
{
	if(students.size() == 0)
	{
		std::cout << "A lonely party consisting of air molecules." 
			  << '\n';
	}

	for(unsigned int i = 0; i < students.size(); ++i)
	{
		std::cout << students[i] << "\n\n";
	}
}

std::ostream& operator << (std::ostream& out, Module modX)
{
	out << "MODULE:" << "\n";

	out << "Module Code: " << std::setfill('0') << std::setw(4) 
	    << modX.getCode() << "\n";
	    
	out << "Module Title: " << modX.getTitle() << "\n\n";

	return out;
}
