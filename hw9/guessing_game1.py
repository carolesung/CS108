#File: guessing_game1.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw9 Part 1
#Date: Feb 15 2018
#Description: Selects random number from 1 to 10 and asks player to guess

import random

def main():
    #Program generats a random number in range 1 to 10 and asks player to guess
    secret = random.randint(1,10)
    guess = int(input("Guess a number from 1 to 10: "))
    #Indefinite loop that keeps going until user guesses correctly
    while guess != secret:
        #Checks whether input is valid
        if guess not in range(1,11):
            print("Invalid guess")
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Guess a number from 1 to 10: "))

    print("Correct!")

main()
