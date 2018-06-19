#File: guessing_game2.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw9 Part 2
#Date: Feb 15 2018
#Description: Player picks a number and program guesses it

print("This program will guess your number in as few guesses as possible.")
lower = int(input("Enter a lower bound: "))
upper = int(input("Enter an upper bound: "))
guess = (lower+upper)//2
count = 1
print("Our guess is", guess)
choice = input("Is that correct (c), too high (h) or too low (l)? ")
#Indefinite loop. Checks whether program guessed user's number correctly
while choice != "c":
    if choice == "h":
        #Updates upper bound
        upper = guess
        #Adjusts guess to the mid-point between higher and lower bounds
        guess = (lower+upper)//2
    else:
    #choice == "l"
        #Updates lower bound
        lower = guess
        #Adjusts guess
        guess = (lower+upper)//2
    print("Our guess is", guess)
    choice = input("Is that correct (c), too high (h) or too low (l)? ")
    count += 1

print("It took",count,"tries to guess your number is",guess,".")
