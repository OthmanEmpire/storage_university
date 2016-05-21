### This program is a number guessing game ###

import random
import time

print("Welcome to Guess How Annoying version 1.0!")
print("I am but a number between 0 and 99. Therefore, who am I?\n\n")

answer = random.randint(0,99)
lives = 5

while(lives > 0):
    guess = int(input("Guess who I am: "))

    if(guess > answer):
        lives = lives - 1 
        print("Too high\nLives remaining: {}\n".format(lives))
        
        
    elif(guess < answer):
        lives = lives - 1
        print("Too low\nLives remaining: {}\n".format(lives))
        
        
    elif(guess == answer):
        print()
        for x in range(3):
            print("Well played!\n")
            time.sleep(1)
        exit()
        
    else:
        print("I didn't see that one coming, I GUESS", end = "")
        for i in range(3):
            print(".")
            time.sleep(1)
