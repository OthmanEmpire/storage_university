'''beetle contains the current state of the beetle'''
beetle = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

'''A lookup for which numbers represent which body part '''
beetleparts = {1:"head", 2:"eye", 3:"antennae", 4:"tail", 5:"leg", 6:"body"}

'''The maximum number of body parts the beetle needs to be complete '''
beetleMaxParts = {1:1, 2:2, 3:2, 4:1, 5:6, 6:1}

    
def rollDice(numberOfRolls):
    ''' Returns a randomly generated psuedo-random number between 1 and 6 (inclusive) '''
    import random
    
    if(numberOfRolls == 1):
        return 1
    else:
        random = random.randint(1,6)
        return random


def finishedBeetle():
    '''Returns True is the beetle is finished and false otherwise '''
    
    if(beetle == beetleMaxParts):
        return True
    else:
        return False
    

def printRules():
    '''Prints out the rules to the game '''
    
    print("\n<<THE RULES>>\n")
    print("Roll the following to obtain:")
    print("6 is for the body, of which there is one.")
    print("5 is for the head, of which there is one.")
    print("4 is for the tail, of which there is one.")
    print("3 is for a leg, of which there are four.")
    print("2 is for an antenna, of which there are two.")
    print("1 is for an eye, of which there are two.\n")


def printWelcome():
    '''Prints out a Welcome message to the game '''
    print("Welcome to Beetle version 1.4!")

    
def printBeetle():
    '''Prints what body parts the beetle currently has '''

    for key in range(1, len(beetle)):

        if(beetle[key] != 0):
            print("You have: ", beetle[key], beetleparts[key])


def updateBeetle(num):
    ''' updates the part list for the beetle'''

    if(beetle[num] != beetleMaxParts[num]):
       beetle[num] += 1
       
        
    
def beetleNeedsPart(num):
    ''' Checks if the beetle needs the body part that has been rolled
        This function shuould return True if the beetle needs the body 
        part and false otherwise'''

    if(beetle[num] == 0):
       return True
    else:
       return False
    
    
def resultOfDiceRoll( diceRoll ):
    '''The game logic to ensure the beetle body parts have their dependencies '''
    print("You got a", beetleparts[diceRoll])

    if  not beetle[6] == 0:
        if not beetle[1] == 0:
            updateBeetle( diceRoll )
        elif ( diceRoll == 1) or (diceRoll > 3):
            updateBeetle( diceRoll )
        else :
            print("Sorry you don't have a head yet")
    elif diceRoll == 6:
        updateBeetle( diceRoll )
    else :
        print("Sorry you don't have a body yet")
            
def runGame():
    '''The game mennu '''
    printWelcome()
    numberOfRolls = 0
    printBeetle()
    while(not finishedBeetle()):
        userResponse = input("Press 'r' to roll the dice, 'h' to display the rules or 'e' to exit \n >")
        if userResponse == 'e':
            break
        elif userResponse == 'h':
            printRules()
        else:
            numberOfRolls = numberOfRolls + 1
            num = rollDice(numberOfRolls)
            print("You rolled a", num)
            resultOfDiceRoll(num)
            printBeetle()
            
    if finishedBeetle():
         print("BEETLE!!!!!!!!!!!!-------You won!!!!!!! in", numberOfRolls , "rolls")
        

runGame()
