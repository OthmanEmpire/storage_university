analyze: analyze.o yeardata.o row.o
	g++ -g -Wall analyze.o yeardata.o row.o -o analyze

analyze.o: analyze.cpp yeardata.hpp row.hpp gnuplot_i.hpp
	g++ -c analyze.cpp

yeardata.o: yeardata.cpp yeardata.hpp
	g++ -c yeardata.cpp

row.o: row.cpp row.hpp
	g++ -c row.cpp

clean: 
	rm -f analyze.o yeardata.o row.o

veryclean: clean
	rm -f analyze
