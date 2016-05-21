#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <vector>

int main()
{
	// Works A.O.K.
	std::ostream_iterator<int> cout(std::cout, " ");
	std::vector<int> vec(3,3);
	std::copy(vec.begin(), vec.end(), cout);
	std::cout << "\n\n" << std::endl;



	// Multiple calls to std::copy don't work, WHY?
	std::string str = "Good Evening, \n\n\n I am but a human, " 
			  "thoroughly, by flesh and bones";
	std::stringstream ss(str);

	std::copy(std::istream_iterator<std::string>(ss),
		  std::istream_iterator<std::string>(),
		  std::ostream_iterator<std::string>(std::cout, " "));
	
	ss.clear();
	ss.seekg(0);

	std::copy(std::istream_iterator<std::string>(ss),
		  std::istream_iterator<std::string>(),
		  std::ostream_iterator<std::string>(std::cout, " "));

	return 0;
}

