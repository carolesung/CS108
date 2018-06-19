#File: checkAge.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw9 Part 0
#Date: Feb 15 2018
#Description: Checks whether user is old enough to drink

def main():
    #Asks for input and returns whether user is old enough to drink
    age = int(input("What is your age? "))
    #Checks whether user's input is higher than or equal to 21 (indefinite loop)
    while age < 21:
        print("Bzzt! You are not old enough to drink.")
        age = int(input("What is your age? "))
    print("Okay! You are old enough to drink.")

main()
