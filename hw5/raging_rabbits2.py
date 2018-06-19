#File: raging_rabbits2.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw7 Part3
#Date: Feb 8 2018
#Description: Lets user guess the correct launch angle to hit the target
#at a random distance

from raging_rabits import *
import random

distance = random.randint(1000,3000)
print("Welcome to Raging Rabbits 2.0!")
print("\nThe target is", distance,"meters away.")
for i in range(5):
    print("You have", 5-i,"guess(es) left.")
    guess = float(input("Make your guess! At what angle would the projectile need to be launched to hit the target? "))
    print("\nPew!")
    diff = distance-compute_projectile_distance(guess)
    if diff in range(-50,50):
        print("\nCongrats, you hit the target!!")
        break
    elif diff > 0:
        print("\nUh oh, the projectile didn't fly far enough.")
        print("The projectile is off by",diff,"meters")
    else:
        print("\nUh oh, the projectile flew too far.")
        print("The projectile is off by",-1*diff,"meters")
        
