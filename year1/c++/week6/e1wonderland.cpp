// Plays a spin-off of a story in Wonderland

#include <iostream>
#include <iomanip>
#include "E1Student.cpp"
#include "E1Module.cpp"


int main()
{

	Module mod1(100, "Feeding");
	
	Student people1("Oz", "Computer Science & Mathematics", 1,
			"King", "Hearts", "Black", 1732050);	
	Student people2("Ozkh", "Unemployed", 0,
			"Joker", "Clubs", "Red", 1732050);
	Student people3("Othman", "Electrical & Electronic Engineering", 1,
			"Five", "Diamonds", "Black", 1732050);
	
	mod1.enrolStudent(people1);
	mod1.enrolStudent(people2);
	mod1.enrolStudent(people3);

	std::cout << "\n" << mod1;
	mod1.printAttendanceRegister();


}
