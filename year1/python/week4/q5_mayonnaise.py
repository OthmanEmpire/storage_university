### This program reads a series of grades from a file then adds them up ###


with open("Q5_friend", "r") as file:

    grades = file.read().split()

    print("Score: ", grades)

    total = 0
    for score in grades:
        total += int(score)

print("The total score is: {}".format(total))
