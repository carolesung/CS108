#File: raging_rabits.py
#Name: Carole (Chia Jung) Sung
#Date: Feb 1 2018
#Assignment: CS 108 Homework 5

import math

#computes the distance (in meters) that a projective will travel, given its initial launch angle theta(in degrees)
def compute_projectile_distance(theta):
    if theta == 180:
        return 0.00
    #Convert angle unit to radians
    theta = math.radians(theta)
    #Compute using given function
    dist = (40000/9.8)*math.sin(2*theta)
    return dist

'''print("\nTest Case 1:")
a = compute_projectile_distance(25)
print("compute_projectile_distance(25)=","%0.2f"%a,"meters.")

print("\nTest Case 2:")
b = compute_projectile_distance(0)
print("compute_projectile_distance(0)=","%0.2f"%b,"meters.")

print("\nTest Case 3:")
c = compute_projectile_distance(170)
print("compute_projectile_distance(170)=","%0.2f"%c,"meters.")'''


#computes the require launch angle (in degrees) to hit a target at a known distance (in meters)
def compute_launch_angle(distance):
    #Compute angle using given function
    ang = 1/2*math.asin((9.8/40000)*distance)
    #Convert angle from radians to degrees
    ang = math.degrees(ang)
    if distance < 0:
        ang = 180 + ang
    return "%0.2f"%ang

'''print("\n\nTest Case 1:")
print("compute_launch_angle(compute_projectile_distance(25))=",compute_launch_angle(a), "degrees.")

print("\nTest Case 2:")
print("compute_launch_angle(compute_projectile_distance(0))=", compute_launch_angle(b), "degrees.")

print("\nTest Case 3:")
print("compute_launch_angle(compute_projectile_distance(170))=", compute_launch_angle(c), "degrees.")
print("\n")'''


#Main function
def main():
    print("Welcome to Raging Rabbits!")
    print("\nThis program will compute the distance the projectile will travel given an angle and vice versa.")
    print("(Positive distances are in front of the cannon and negative distances are behind the cannon.)")
    #Get angle input from user
    angle = float(input("\nAt what angle would you like to fire the projectile in degrees? (Input a number between 0 and 180) "))
    dist = compute_projectile_distance(angle)
    print("Pew! Your projectile flew","%0.2f"%dist,"meters.")

    #Get distance input from user
    dist = float(input("\nAt what distance is the object you're trying to hit? "))
    angle = compute_launch_angle(dist)
    print("You'll need to fire your projectile at an angle of", angle, "degrees to hit the object.")   
    print("\n")

#main()
