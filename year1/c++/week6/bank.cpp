// Implementation of a simple bank account class
// (NDE, 2015-02-07)

#include "bank.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;


// Overloaded constructors

BankAccount::BankAccount(const string& id, const string& nm):
  identifier(id), name(nm), balance()
{
  if (identifier.size() == 0) {
    throw invalid_argument("empty account ID");
  }

  if (name.size() == 0) {
    throw invalid_argument("empty account name");
  }
}


BankAccount::BankAccount(const string& id, const string& nm, const Money& bal):
  identifier(id), name(nm), balance(bal)
{
  if (identifier.size() == 0) {
    throw invalid_argument("empty account ID");
  }

  if (name.size() == 0) {
    throw invalid_argument("empty account name");
  }
}

void BankAccount::deposit(const Money& depositAmount)
{
	balance = balance + depositAmount;
}

bool BankAccount::withdraw(const Money& withdrawAmount)
{
	Money remaining	= balance - withdrawAmount;

	if(remaining < Money(0,0))
	{
		cout << "BLACKHOLE!" << '\n';
		return false;
	}
	else
	{
		balance = balance - withdrawAmount;
		cout << "Withdrawing:\n" << withdrawAmount << "\n\n"
		     << "Remaining amount:\n" << get_balance() << "\n\n";

		return true;
	}
}
