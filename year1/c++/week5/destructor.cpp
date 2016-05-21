#include <iostream>
#include <stdexcept>

class Banana
{
	public:
		// Constructors
		Banana(): fruity(0), juicy(0), SIZE(1024), arr(new int[SIZE]) {}
		Banana(int fu, int ju): fruity(fu), juicy(ju), SIZE(1024), \
					arr(new int[SIZE]) {}
		
		// Copy constructor
		Banana(const Banana& apple): fruity(apple.fruity), SIZE(1024), arr(new int[SIZE]) {}

		// Destructor
		~Banana() {std::cout << "GG"; delete [] arr;}

		// Access data
		const int& content() const {return fruity;}

		// Move assignment
		Banana& operator = (Banana& apple)
		{
			delete [] apple.arr;
			fruity = apple.fruity;
			apple.fruity = 0;
			return *this;
		}

	private:
		int fruity;
		int juicy;
		const int SIZE;
		int* arr;
};

int main()
{
	Banana mushy;
	Banana expired(4,2);
	mushy = expired;


	std::cout << "Expired: " << expired.content() << std::endl;
	std::cout << "Expired: " << mushy.content() << std::endl;

	return 0;

}
