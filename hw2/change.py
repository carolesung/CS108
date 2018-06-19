'''
Author:Carole(Chia Jung) Sung
Email: carole07@bu.edu
Task: Write a program that, given a price in cents that is less than a dollar (i.e., 100 cents), determines the
method of giving change that uses the fewest coins. '''

def LeastDollarChange():
    price = 67
    change = 100-67
    print("The price of your item is", price, "cents, and your change is",change,"cents.")
    quarters = change//25
    remainder = change % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    remainder = remainder % 5
    pennies = remainder
    print("\nHere's the change that uses the fewest coins:")
    print("\n  pennies:  ", pennies)
    print("  nickels:  ", nickels)
    print("  dimes:    ", dimes)
    print("  quarters: ", quarters)
    print("\n")
