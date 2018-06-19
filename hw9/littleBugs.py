#File: littleBugs.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw9 Part 3
#Date: Feb 15 2018
#Description: Implements a variation of the "99 bottles of beer" song

import random

def main():
    #Program picks random numbers of bugs between 42 and 137 and prints out the verse
    #of the song using the number. Only stops if number is 42
    bugs = random.randint(42,137)
    while bugs != 42:
        #Indefinite loops only stops when bugs==42
        print("\n")
        print(bugs,"little bugs in the code,")
        print(bugs,"little bugs.")
        print("Take one down, patch it around,")
        #Chooses new number of bugs
        bugs = random.randint(42,137)
        print(bugs, "little bugs in the code....")

    print("\nDebugging is so much fun!!")

main()
