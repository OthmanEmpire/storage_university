for i in {1..10} 
do
    mpicc -Wall -g -o coursework coursework.c
    mpirun -np 10 -hosts comp-pc3009:4,comp-pc3007:4,comp-pc3006:2 ./coursework 100000000 
done
