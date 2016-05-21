#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iterator>
#include <algorithm>
#include <vector>
#include <time.h>


void generateFile(char* fileName)
{
	std::ofstream outFile;

	std::string str = "Amorphous Borium Can Electrocute";
	std::stringstream ss(str);

	// Open file
	
	outFile.open(fileName);
	if(not outFile)
	{
		std::cerr << "ERROR: Could not write to file! " << std::endl;
		return;
	}

	// Write a string onto the screen and into a file as well

	std::cout << "Writing to file '" << fileName << "':" << std::endl;
	std::cout << str << std::endl;
	outFile << str << std::endl;

}

std::vector<std::string> readFile(char* fileName)
{
	std::vector<std::string> wordsVec;
	std::ifstream inFile;
	std::string word;

	// Read file
	
	inFile.open(fileName);
	if(not inFile)
	{
		std::cerr << "ERROR: Could not open file! " << std::endl;
		return wordsVec;
	}

	while(inFile >> word)
	{
		wordsVec.push_back(word);
	}

	return wordsVec;
}

void writeFile(char* fileName, std::vector<std::string> wordsVec)
{
	std::ofstream outFile;
	std::vector<std::string>::iterator wordsItr;

	// Opens file to be written to

	outFile.open(fileName, std::ofstream::trunc);
	if(not outFile)
	{
		std::cerr <<  "ERROR: Could not write to file! " << std::endl;
		return;
	}

	for(wordsItr = wordsVec.begin(); wordsItr != wordsVec.end(); ++wordsItr)	{
		outFile << *wordsItr << std::endl;
	}
}

int main(int argc, char* argv[])
{
	std::vector<std::string> wordsVec;
	std::vector<std::string>::iterator wordsItr;

	// Seeding the random shuffler

	std::srand(time(NULL));

	if(argc != 3)
	{
		std::cerr << "ERROR: Please input two file names only! " 
			  << std::endl;
		return 1;
	}

	generateFile(argv[1]);
	wordsVec = readFile(argv[1]);

	for(wordsItr = wordsVec.begin(); wordsItr != wordsVec.end(); ++wordsItr)
	{
		std::random_shuffle((*wordsItr).begin(), (*wordsItr).end());
		std::cout << *wordsItr << std::endl;
	}
	writeFile(argv[2], wordsVec);

	return 0;
}
