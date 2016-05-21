// Creating the dreadful diamond to better understand multiple inheritance

#include <iostream>
#include "E2Fairytale.hpp"
#include "E2Horror.hpp"
#pragma once

class DD: public Fairytale, public Horror
{
	public:
		int sanityPoints = 5;
};


int main()
{
	DD rogueKnight;

	std::cout << rogueKnight.sanityPoints;
	std::cout << rogueKnight.sanityPoints;

}
