// Implementation file for a simple Money class - see also money.hpp
// (NDE, 2015-01-08)

#include "moneys.hpp"
#include <stdexcept>
#include <iostream>
#include <iomanip>

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


Money Money::operator + (const Money& m1)
{
  int sum = m1.as_cents() + this->as_cents();

  int euros = sum / 100;
  int cents = sum % 100;

  return Money(euros, cents);
}

ostream& operator << (ostream& out, const Money& m)
{
	char old_fill = out.fill('0');

	out << m.get_euros() << '.'<< setw(2) << m.get_cents();

	out.fill('c');

	return out;
}

istream& operator >> (istream& in, Money& m)
{
	double value;
	in >> value;

	int value_in_cents = int(value*100);

	m.euros = value_in_cents / 100;
	m.cents = value_in_cents % 100;

	return in;
}
