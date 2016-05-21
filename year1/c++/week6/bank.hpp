// Header file for a simple bank account class
// (NDE, 2015-02-07)

#pragma once

#include <string>
#include "money.hpp"

class BankAccount
{
  public:
    BankAccount(const std::string&, const std::string&);
    BankAccount(const std::string&, const std::string&, const Money&);
    std::string get_identifier() const { return identifier; }
    std::string get_name() const { return name; }
    Money get_balance() const { return balance; }
    void deposit(const Money&);
    bool withdraw(const Money&);

  protected:
    std::string identifier;
    std::string name;
    Money balance;
};
