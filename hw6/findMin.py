#File: findMin.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw6 Part1
#Date: Feb 6 2018
#Description: Contains a function that takes 3 parameters and returns the minimum

def find_min(a,b,c):
    #Takes 3 parameters and returns the minimum of the three
    if a > b:
        
        if b > c:
            #a > b so if b > c then c is minimum
            return c
        else:
            #Otherwise b is minimum
            return b
    else:
        if a > c:
            return c
        else:
            return a
    
print('find_min(1,2,3)', find_min(1,2,3))
print('find_min(3,2,1)', find_min(3,2,1))
print('find_min(1,2,1)', find_min(1,2,1))
print('find_min(3,2,3)', find_min(3,2,3))
print('find_min(2,2,3)', find_min(2,2,3))
print('find_min(3,2,2)', find_min(3,2,2))
