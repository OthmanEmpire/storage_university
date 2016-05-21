### I am but the median. ###

import math


def median(numbers):

    n = len(numbers)
    pos_median = int(n/2)

    if(n%2 == 0):
        i = int(math.floor(pos_median))
        median = (int(numbers[i-1]) + int(numbers[i]))/2
        return median
    else:
        median = numbers[pos_median]
        return median 

        
print("I am but the median.")
numbers = input("Please input a list of numbers (e.g. 1,2,3,4,5): ").split(',')

median = median(numbers)
print(median)
