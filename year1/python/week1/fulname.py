### This program prompts the user for his/her fullname ###
###(recapitalizes if need be) and then greets them ###

print("Welcome to ask your first & last name and THEN greet you, version 1.0, ")
print("the first and last version!\n")

print("Please input your first name now: ", end = " ")
first = input()
first = first.capitalize()

print("Please input your last name now: ", end = " ")
last = input()
last = last.capitalize()

print("Suprise, suprise! Your full name is: ", first, " ", last, end = ", ", sep ='')
print("what a shock!\n\nGoodbye ", first, last, " ! ! !", sep=' ')
