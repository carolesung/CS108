'''
Author: Carole(Chia Jung) Sung
Email: carole07@bu.edu
Task: Create a program called stats.py that will calculate and print out
some statistical measures of a sequence of five numbers, specifically their
(i) sum, (ii) arithmetic mean (or average), (iii)variance, and
(iv) standard deviation.'''

def stats():
    a = 8
    b = 9
    c = 10
    d = 9
    e = 8

    sumNum = a+b+c+d+e
    mean = sumNum/5
    var = ((a-mean)**2+(b-mean)**2+(c-mean)**2+(d-mean)**2+(e-mean)**2)/5
    std = var **0.5

    print("sum: ",sumNum)
    print("mean: ",mean)
    print("variance: ",var)
    print("standard dev: ",std)
