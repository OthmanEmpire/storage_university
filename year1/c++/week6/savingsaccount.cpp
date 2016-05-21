// A type, of many types, of bank accounts

#include "bank.hpp"
#include "savingsaccount.hpp"


SavingsAccount::SavingsAccount(const std::string& identifier_,
				const std::string& name_,
				const double rate_):
			BankAccount(identifier_, name_), rate(rate_) {};

SavingsAccount::SavingsAccount(const std::string& identifier_,
				const std::string& name_,
				const Money& money_,
				const double rate_):
			BankAccount(identifier_, name_, money_), rate(rate_) {};

void SavingsAccount::addInterest() 
{
	int newAmount, eurosAfterInterest, centsAfterInterest;

	newAmount = balance.as_cents() * (1 + rate);

	eurosAfterInterest = newAmount / 100;
	centsAfterInterest = newAmount % 100;
	
	balance = Money(eurosAfterInterest, centsAfterInterest);
}

