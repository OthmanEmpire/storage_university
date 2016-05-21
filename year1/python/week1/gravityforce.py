### This program calculates the force of gravity between two objects after ###
### obtaining user inputted data of distance and masses of both objects ###



print("Welcome to Gravity, may the Force be with you.")
print("Please input the following parameters to calculate F: ")

# Absorbing the data to substitute in the forumla
print("Mass of object A in kg: ", end = " ")
massA = float( input() )

print("Mass of object b in kg: ", end = " ")
massB = float( input() )

print("Distance between these so called objects in meters: ", end = " ")
distance = float( input() )

G = 6.67 * 10 ** -11

force = G * (massA * massB) / distance**2

print("The force in your hypothetical scenario is: ", force, end = " N")
