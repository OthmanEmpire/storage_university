#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>


void chopIt(std::vector<int> &vec)
{
	std::vector<int>::iterator vecItr;

	for(vecItr = vec.begin(); vecItr != vec.end(); ++vecItr)
	{
		if(*vecItr < 0)
		{
			*vecItr = 0;
		}
		else if(*vecItr > 100)
		{
			*vecItr = 100;
		}
	}
}

int main()
{
	std::vector<int> vec(11, 12);
	std::ostream_iterator<int> out(std::cout, ", ");
	
	std::cout << "\nInitial Vector: " << std::endl;
	vec[0] = -8;
	vec[10] = 800;
	std::copy(vec.begin(), vec.end(), out);

	std::cout << "\n\nChopped Vector: " << std::endl;
	chopIt(vec);
	std::copy(vec.begin(), vec.end(), out);

	return 0;
}
