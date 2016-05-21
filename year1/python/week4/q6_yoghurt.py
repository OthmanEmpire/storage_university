### This program yogHURTS ###

with open("Q5_friend", "r") as file:

    lines = 0
    while True:
    
        n = file.readline()

        if(n == ''):
            break
        else:
            lines += 1

print("The number of lines are:", lines)
