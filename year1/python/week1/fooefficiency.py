# This program calculates the cost of pizza per square centimeter #

print("Welcome to food efficiency version 1.0.0.0.0, the inefficient version!")
print("This version solely focuses on the food item known as 'Pizza'\n")

print("Please input your the radius of your perfectly circular pizza in cm: ", end = " ")
radius = float( input() )

print("Now please input the cost of your pizza in SR: ", end = " ")
cost = float( input() )

pi = 3.1415926535       # Nice approximation...
unitcost = cost / (pi * radius**2)

print("The food efficiency of your pizza is: ", unitcost, end = " SR/cm^2")
