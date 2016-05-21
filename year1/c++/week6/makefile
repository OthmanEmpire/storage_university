# BankAccount example

testbank: testbank.o bank.o money.o savingsaccount.o
	g++ testbank.o bank.o money.o savingsaccount.o -o testbank

testbank.o: testbank.cpp bank.hpp
	g++ -c testbank.cpp

bank.o: bank.cpp bank.hpp
	g++ -c bank.cpp

money.o: money.cpp money.hpp
	g++ -c money.cpp

savingsaccount.o: savingsaccount.cpp savingsaccount.hpp
	g++ -c savingsaccount.cpp

# Rectangle example

testrect: testrect.o rect.o
	g++ testrect.o rect.o -o testrect

testrect.o: testrect.cpp rect.hpp
	g++ -c testrect.cpp

rect.o: rect.cpp rect.hpp shape.hpp
	g++ -c rect.cpp

# Clean-up

clean:
	del testbank.o bank.o money.o testrect.o rect.o

veryclean: clean
	del testbank.exe testrect.exe
