### This program finds the factorial of a non-negative number ###

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n*factorial(n-1)



x = int(input("Welcome to Fractals version 1.2.8.4.7.2! Please input your digit: "))
print("Factorial of {} is {}".format(x, factorial(x)))
