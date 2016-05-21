// A type, of many types, of bank accounts

#include "bank.hpp"


class SavingsAccount: public BankAccount
{
	public:
		SavingsAccount(const std::string& identifier,
				const std::string& name,
				const double rate);

		SavingsAccount(const std::string& identifier,
				const std::string& name,
				const Money& money,
				const double rate);

		double getRate() const {return rate;}	
		void addInterest();

	private:
		double rate;
};
