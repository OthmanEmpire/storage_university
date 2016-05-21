// Header file for a simple Money class - see also money.cpp
// (NDE, 2015-01-08)

#include <iostream>
#pragma once


class Money
{
  public:
    Money(): euros(0), cents(0) {}
    Money(int, int);
    int get_euros() const { return euros; }
    int get_cents() const { return cents; }
    int as_cents() const { return 100*euros + cents; }

  private:
    int euros;
    int cents;
};

bool operator < (const Money&, const Money&);
Money operator + (const Money&, const Money&);
Money operator - (const Money&, const Money&);
std::ostream& operator << (std::ostream&, const Money&);
