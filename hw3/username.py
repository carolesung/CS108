'''
Author: Carole (Chia Jung) Sung
Email: carole07@bu.edu
Task: program that creates usernames based on a person’s full name.
The program will produce a customized greeting using the names,
as well as generate an 8-character username.'''

last = input("Enter your last name: ")
first = input("Enter your first name: ")
middle = input("Enter your middle name: ")
print("Welcome,", first, last +".")
#index = len(last)%
username = first[0]+middle[0]+last[:6]
print("Your username is",username+".")
