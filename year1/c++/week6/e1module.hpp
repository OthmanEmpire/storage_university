// A party formed by several students

#pragma once

#include <iostream>
#include <string>
#include <vector>
#include "E1Student.hpp"


class Module
{
	public:
		Module(int code_, std::string title_):
			code(code_), title(title_) {}

		int getCode() const {return code;}
		std::string getTitle() const {return title;}

		void enrolStudent(Student people1);
		void printAttendanceRegister();
		

	private:
		int code;
		std::string title;

		std::vector<Student> students;
};

std::ostream& operator << (std::ostream& out, Module modX);
