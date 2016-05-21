// Implementation file for a simple Money class - see also money.hpp
// (NDE, 2015-01-08)

#include "money.hpp"
#include <stdexcept>
#include <iostream>

using namespace std;


Money::Money(int eur, int cen)
{
  if (eur < 0) {
    throw invalid_argument("invalid number of euros");
  }

  if (cen < 0 or cen > 99) {
    throw invalid_argument("invalid number of cents");
  }

  euros = eur;
  cents = cen;
}


bool operator < (const Money& m1, const Money& m2)
{
  int diff = m1.get_euros() - m2.get_euros();

  if (diff == 0) {
    diff = m1.get_cents() - m2.get_cents();
  }

  return diff < 0;
}


Money operator + (const Money& m1, const Money& m2)
{
  int sum = m1.as_cents() + m2.as_cents();

  int euros = sum / 100;
  int cents = sum % 100;

  return Money(euros, cents);
}


Money operator - (const Money& m1, const Money& m2)
{
  int sum = m1.as_cents() - m2.as_cents();

  if (sum < 0) {
    throw range_error("cannot have negative amounts of Money!");
  }

  int euros = sum / 100;
  int cents = sum % 100;

  return Money(euros, cents);
}

ostream& operator << (ostream& out, const Money& m1) 
{
	out << "Euros: " << m1.get_euros() << '\n'
	    << "Cents: " << m1.get_cents();

	return out;
}
