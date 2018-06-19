#File: validDate.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw6 Part3
#Date: Feb 6 2018
#Description: Contains a function that takes parameters for the month, day, year and returns the boolean constant True if it's valid and False otherwise.

def valid_date(month, day, year):
    #Returns True if given a valid date and returns False otherwise.
    month31 = (1,3, 5, 7, 8, 10, 12)
    month30 = (4,6,9,11)
    #Checks if given month is in the sequence of months that have 31 days
    if month in month31:
        #Returns whether day is in valid range (boolean)
        return day <= 31
    #Checks if given month is in the sequence of months that have 30 days
    elif month in month30:
        #Returns whether day is in valid range (boolean)
        return day <= 30
    #Checks case for month of february
    elif month == 2:
        
        if year % 4 == 0 and year %400 == 0:
            #Leap year
            return day <= 29
        else:
            return day <= 28
    else:
        return False

########################################
    
print("Test Cases:")
print("valid_date(2,7,2017):",valid_date(2,7,2017))
print("valid_date(2,29,2017):",valid_date(2,29,2017))
print("valid_date(1,32,2017):",valid_date(1,32,2017))
print("valid_date(13,7,2017):",valid_date(13,7,2017))
print("valid_date(4,31,2017):",valid_date(4,31,2017))
print("valid_date(5,24,2008):",valid_date(5,24,2008))

