#include <iostream>
#include <algorithm>

int dice_score(int quantity=2)
{
	int sum = 0;

	for(int i = 0; i < quantity; ++i)
	{
		sum = sum + rand()%6 + 1;
	}

	return sum;
}

int main()
{
	
	std::cout << dice_score(200) << std::endl;

}
