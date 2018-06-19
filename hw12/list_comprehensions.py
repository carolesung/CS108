#File: list_comprehensions.py
#Name: Carole (Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: CS108 A12
#Date: Feb 28 2018
#Description: Assignment 12 includes multiple list comprehension functions

def triple(values):
    '''Processes a sequence of values and returns a list containing the triple
    of each original value'''
    lst = []
    for i in values:
        lst.append(i*3)
    return lst

print("Test Case #1:")
print(triple([1,2,3]))
print(triple(['a','b','c']))
print(triple(['python']))
print(triple('python'))


################################################################

def powers(b,n):
    '''Returns the first n powers of base b'''
    lst = []
    for i in range(n):
        lst.append(b**i)
    return lst

print("\nTest Case #2:")
print(powers(2,10))
print(powers(3,8))

################################################################

def divisors(n):
    '''Returns a list containing all the divisors (without remainder)
    of the integer n'''
    lst = []
    for i in range(1, n+1):
        if n%i == 0:
            lst.append(i)
    return lst

print("\nTest Case #3:")
print(divisors(10))
print(divisors(60))
print(divisors(3147))
print(divisors(2017))

###################################################################

def string_to_ascii(s):
    '''Returns a list of the ASCII codes corresponding to a string s'''
    lst = []
    for l in s:
        lst.append(ord(l))
    return lst

print("\nTest Case #4:")
print(string_to_ascii('whatever'))
print(string_to_ascii('try everything'))

#####################################################################

def ascii_to_string(ascii_codes):
    '''Returns the string corresponding to the list of the ASCII codes'''
    s = ""
    for code in ascii_codes:
        s += chr(code)
    return s

print("\nTest Case #5:")
print(ascii_to_string([116,114,121]))
print(ascii_to_string([119,104,97,116,101,118,101,114]))
lst = [89,111,117,32,116,111,111,32,99,97,110,32,119,114,105,116,101,32,99,114,121,112,116,105,99,32,109,101,115,115,97,103,101,115,32,105,110,32,65,83,67,73,73,32,99,111,100,101,115,33]
print(ascii_to_string(lst))





    
