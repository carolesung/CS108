#File: lab_exam2.py
#Name: Carole (Chia Jung) Sung
#Date: Feb 21 2018
#Description: The second lab exam for CS108

def old_enough(age):
    #takes age for parameter and returns a string describing the activities
    #one can do at that age
    if age >= 21:
        #checks if age is greater than 21
        return "you can drink alcohol."
    elif age < 16:
        #checks if age is less than 16
        return "you can ride a skateboard."
    else:
        return "you can drive a car."

print("Test Cases #1:")
print(old_enough(21))
print(old_enough(12))
print(old_enough(16))
print("\n")
##################################

def print_multiples(n):
    #calculates and prints the first 10 multiples of n
    for i in range(10):
        #prints number all in same line
        print(i*n, end= " ")
        
print("Test Cases #2:")
print_multiples(2)
print("\n")
print_multiples(5)
print("\n")
print_multiples(0)
print("\n")
print_multiples(-1)
print("\n")
###################################

def sum_between(start, end):
    #calculates and returns the sum of all integers between start and end inclusive
    s = 0
    for i in range(start,end+1):
        #goes from start to end inclusive
        s = s+i
        #accumulator
    return s

print("Test Cases #3:")
print(sum_between(3,9))
print(sum_between(0,3))
print(sum_between(1,10))
print(sum_between(8,9))

