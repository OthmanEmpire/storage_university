### This program generates the nth Fibonacci number :o ###


def Fibo(n):
    if(n == 0):
       return 0
    if(n == 1):
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

x = input("Welcome to the Fibonacci nth Number version 1.0! Please input data: ")
x = int(x)

print(Fibo(x))
