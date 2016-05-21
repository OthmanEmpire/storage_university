// A program to simulate rolling of a pair of six-sided dice
// (NDE, 2014-12-11)

#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

int dice_score();

int main()
{
	srand(time(NULL));

	for(int i = 0; i < 5; ++i)
	{
		cout << "Score of two dice rolled: " << dice_score() << endl;
	}
}

int dice_score()
{
 int roll1 = rand() % 6 + 1;
 int roll2 = rand() % 6 + 1;
 return roll1 + roll2;
}

