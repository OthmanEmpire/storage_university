### This program compares modes "w" & "a" of the function open() ###

with open("Q3_squares", "w") as file:
    
    for x in range(101):
        y = x**2
        file.write("{} ---> {},\n".format(x,y))
