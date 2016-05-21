### This program finds the mean and median and then compares them ###

import math


def median(numbers):

    n = len(numbers)
    pos_median = int(n/2)

    if(n%2 == 0):
        i = int(math.floor(pos_median))
        median = (int(numbers[i-1]) + int(numbers[i]))/2
        return median
    else:
        median = int(numbers[pos_median])
        return median 



def mean(numberlist):

    sum = 0
    n = len(numberlist)

    for i in range(n):
        sum += int(numberlist[i])

    mean = sum / n
    
    return mean



list = []
number = 0

print("Welcome to mean and median version 1.0! The new mode.\n")

while(True):

    number = input("Please input a number in your list: ")

    if(number == 'end'):
        break
    else:
        list.append(number) 


mean = mean(list)
median = median(list)
print("\n\nMean: {:f}, Median: {}".format(mean, median))

difference = math.fabs(mean - median)

if(mean > median):
    print("Mean is greater by: {}".format(difference))
elif(median < mean):
    print("Median is greater by: {}".format(difference))
else:
    print("Both are equal")
    
