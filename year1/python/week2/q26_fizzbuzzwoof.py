### Count until 100 and replace: 3k = Fizz ; 5k = Buzz ;  3m and 5n = FizzBuzz ###

import time
import random
import sys



def loading(x):
    print("\nWhile waiting, please KINDLY realize that:\n")
    print("\'Fizz\' for multiples of 3\n\'Buzz\' for multiples of 5\n\'Woof\' for multiples of 7")
    print("\'FizzBuzz\' for multiples of 3 and 5\n\'FizzWoof\' for multiples of 3 and 7\n\'BuzzWoof\' for multiples of 5 and 7")
    print("\'FizzBuzzWoof\' for multiples of 3 and 5 and 7")
    print("\nLOADING", end = "")
    
    for i in range(7):
        print(".", end = "")
        time.sleep(x/7)     # To make the total loading time in seconds equal to the argument of the function def
    print()



def start():
    start = input("\nAre you willing to draw first blood? (Y/N): ")
    print()
    if(start == 'Y'):
        return 1

    elif(start == 'N'):
        return 0
    else:
        print("\nGG\n")
        exit



def calculator(n):
    mod3 = n%3
    mod5 = n%5    
    mod7 = n%7

    if(mod3 == 0 and mod5 == 0):
        return "FizzBuzz"

    elif(mod3 == 0 and mod7 == 0):
        return "FizzWoof"

    elif(mod5 == 0 and mod7 == 0):
        return "BuzzWoof"

    elif(mod3 == 0 and mod5 == 0 and mod7 == 0):
        return "FizzBuzzWoof"
        
    elif(n%3 == 0):
        return "Fizz"
              
    elif(n%5 == 0):
        return "Buzz"

    elif(n%7 == 0):
       return "Woof"
    
    else:
        return n


    
def myturn(n):
    guess = input("Your turn for number {}: ".format(n))
    return guess



def pcturn(n):
    print("\nMy turn to for number {}\n".format(n), end = "")
    print("Now calculating your impending doom", end = "")
    
    for i in range(3):
        print(".", end = "")
        time.sleep(1)
    print()

    mistake = random.randint(1,20)

    if(mistake != 1):
        answer = calculator(n)
        print("Solution found: {}\n\n".format(answer), end = "")
        
    else:
        print("POLYTETRAFLUORETHYLENE")
        print("\n\nApparently my guess was incorrect; you win.")
        exit(0)



def checker(guess, n):
    answer = calculator(n)

    if(guess == str(answer)):
        print("\'{}\' was correct.\n".format(guess))
    else:
        print("What a loser. The answer was OBVIOUSLY: {}".format(answer))
        exit(0)




print("Welcome to compete against FizzBuzz Bot Serial Number PK-209-3.14159X!")
print("We will commence mortal kombat shortly...")
time.sleep(2)
loading(7)

start = start()
if(start == 1):
    for n in range(1, 101, 2):      # Ignores 0 since 0%3 and 0%5 result in FizzBuzz while 0 is not a factor of 3

        guess = myturn(n)
        checker(guess, n)
        pcturn(n + 1)
        
else:
    for n in range(1,101, 2):

        pcturn(n)
        guess = myturn(n + 1)
        checker(guess, n + 1)
