#include <iostream>
#include "bank.hpp"
#include "savingsaccount.hpp"


int main()
{
//	BankAccount B1("11235", "Oz", Money(42,14));
//	BankAccount B2("81321", "Zo");
	SavingsAccount B3("345589", "Ozkh", Money(20,40), 2.71828);
	
//	std::cout << B1.get_balance() << "\n\n";
//	std::cout << B2.get_balance() << "\n\n";

//	B1.withdraw(Money(17,32));
//	B2.withdraw(Money(0,0));

//	B1.deposit(Money(17,32));
//	B2.deposit(Money(1,1));

//	std::cout << B1.get_balance() << "\n\n";
//	std::cout << B2.get_balance() << "\n\n";

	std::cout << "Savings BEFORE Account:\n" << B3.get_balance() << "\n"
		  << "Interest rate: " << B3.getRate() << "\n\n";

	B3.addInterest();

	std::cout << "Savings AFTER Account:\n" << B3.get_balance() << "\n"
       		  << "Interest rate: " << B3.getRate() << "\n\n";

}
