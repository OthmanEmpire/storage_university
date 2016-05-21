### This program reads lines from a file ###


with open("Q3_mustard.py", "r") as file:

    while True:
        line = file.readline()

        if(line == ""):
            break
        else:
            print(line)
            
