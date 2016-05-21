### This program expands a complex number z = (a + bi)^n ###


a, b, n = input("Coefficients of z & radical: ").split()

a = int(a)
b = int(b)
n = int(n)


for n in range(n//2):
    
    real = a**2 - b**2
    imaginary = 2*a*b



print("{} + {}i".format(real, imaginary))
