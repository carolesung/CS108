#File: lab_exam1.py
#Name: Carole (Chia Jung) Sung
#Date: Feb 7 2018
#Description: (Lab Exam 1) Contains three functions which calculates the cost of a pizza
#per sq in, returns the outer characters of a given string and returns the
#factorial of a given input

import math

def pizza_cost_per_sq_in(diameter, price):
    #calculates and returns the cost of a pizza per square inch
    r = diameter / 2
    #Calculate area using given function
    a = math.pi*(r**2)
    #Calculate cost per square inch using given function
    cost = price/a
    return cost

'''#Test Cases
print("Test Cases:")
print("pizza_cost_per_sq_in(12, 10.00): ",pizza_cost_per_sq_in(12, 10.00))
print("pizza_cost_per_sq_in(16, 15.00): ", pizza_cost_per_sq_in(16, 15.00))
print("pizza_cost_per_sq_in(20,0): ", pizza_cost_per_sq_in(20,0))'''

###############################

def outer_chars(s,n):
    #returns a string that contains the first and last n characters of the original string s
    if n > len(s):
        #Handles case where string index is out of range
        return s
    #Concatenates first n characters and last n characters and stores in variable ret
    ret = s[:n]+s[-n:]
    return ret

'''#Test Cases
print("Test Cases:")
print("outer_chars('hello goodbye',2)",outer_chars("hello goodbye",2))
print("outer_chars('computer science',4)",outer_chars("computer science",4))
print("outer_chars('hello',10)", outer_chars("hello",10))'''

##################################

def facts_are_cool():
    #asks user for a number, calculates and prints the factorial of the input
    #Welcome message
    print("This program finds the factorial of a number")
    #stores user input in variable num
    num = int(input("\nEnter a positive integer: "))
    #Calculate factorial with help of math library
    fact = math.factorial(num)
    print("The factorial is",fact)

