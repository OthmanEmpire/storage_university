### This program reads a series of grades from a file then adds them up ###

def chooseFromThreeChoices(choices):
    
    import time
    
    while True:
            try:
                print("Choose your destiny:")
                print("A.", choices[0])
                print("B.", choices[1])
                print("C.", choices[2])
                      
                option = input()
                
                if(option.capitalize() == 'A'):
                    return '1'
                elif(option.capitalize() == 'B'):
                    return '2'
                elif(option.capitalize() == 'C'):
                    return '3'
                else:
                    raise NameError

            except NameError:
                print("Beware of imminent supermassive blackholes ", end = "")
                print("in your backyard", end = "")
                for seconds in range(3):
                    time.sleep(1)
                    print(".", end = "")
                print("\n")
                    


def gradeCalc(file_name):

    while True:
        
        try:
            with open(file_name, "r") as file:
                    
                grades = file.read().split()

                total = 0
                for score in grades:
                    total += int(score)

                return grades, total

        except IOError as err:
            print("{}\n".format(err))
            file_name = input("Please input your file name again: ")
            



print("Welcome to Lithium Permanganate, version 1.2.1!")
print("You will now be subjugated.\n")

choices = \
(
"Use default file, 'Q5_friend'",
"Input a different file name",
"Noob around"
)

choice = chooseFromThreeChoices(choices)

if(choice == '1'):
    data_file = "Q5_friend"
    
elif(choice == '2'):
    data_file = input("Please input the name of your file: ")
    
else:
    print("\n\n___THS PRGM IS SRS BSNS___\n\n")
    exit()


grades, total = gradeCalc(data_file)
print()
print("Score: ", grades)
print("The total score is: {}".format(total))
