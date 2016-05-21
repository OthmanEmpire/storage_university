### This program calculates the mean of the numbers ###

def mean(numberlist):

    sum = 0
    n = len(numberlist)

    for i in range(n):
        sum += int(numberlist[i])

    mean = sum / n
    
    return mean

print("Welcome to mean, the mean version.")
numbers = input("Please input your list of numbers (e.g. 1,2,3): ").split(',')

mean = mean(numbers)
print("{:.1f}".format(mean))
