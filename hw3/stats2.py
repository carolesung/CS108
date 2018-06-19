'''
Author: Carole(Chia Jung) Sung
Email: carole07@bu.edu
Task: Create a program called stats2.py that will calculate and print out
some statistical measures of a sequence of five numbers, given by user, specifically their
(i) sum, (ii) arithmetic mean (or average), (iii)variance, and
(iv) standard deviation.'''

def stats2():
    print("Welcome! Please enter five numbers, one at a time, to calculate the sum, mean, variance, and standard deviation")
    a = float(input("Input first number: "))
    b = float(input("Input second number: "))
    c = float(input("Input third number: "))
    d = float(input("Input fourth number: "))
    e = float(input("Input fifth number: "))

    sumNum = a+b+c+d+e
    mean = sumNum/5
    var = ((a-mean)**2+(b-mean)**2+(c-mean)**2+(d-mean)**2+(e-mean)**2)/5
    std = var **0.5

    print("sum: ",sumNum)
    print("mean: ",mean)
    print("variance: ",var)
    print("standard dev: ",std)
