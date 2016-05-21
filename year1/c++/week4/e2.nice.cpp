#include <iostream>
#include <cstdlib>
#include <time.h>

int dice_score(int quantity)
{
	int sum = 0;

	for(int i = 0; i < quantity; ++i)
	{
		sum = sum + rand() % 6 + 1;
	}	

  return sum; 
}

int main()
{
	int quantity = 0;
	int score = 0;

	srand(time(NULL));

	std::cout << "Welcome to D.I.C.E, version N.I.C.E 3.1.4\n"
		  << "Please input the amount of times to roll: ";
	std::cin >> quantity;

	score = dice_score(quantity);

	std::cout << "Your 'score' is: " << score << std::endl;

	return 0;
}
