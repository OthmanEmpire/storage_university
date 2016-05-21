# This program calculates the distance a car can travel without refueling #
# after obtaining data on the tank size and distance travelled per litre #

print("Welcome to 'How far can you go without losing hope?', version 1.0")
print("Please input the following parameters so estimate the distance")
print("your car can travel with a known quantity of fuel: ")

print("Your tank's capacity in litres: ", end = " ")
capacity = float( input() )

print("The distance travelled in km by your car per litre of fuel: ", end = " ")
perlitre = float( input() )


distance = capacity * perlitre
print("Therefore, you can only go ", distance, " km without losing hope!\n")
print("Goodbye!")


