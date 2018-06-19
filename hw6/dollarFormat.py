#File: dollarFormat.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw6 Part2
#Date: Feb 6 2018
#Description: Contains a function that returns a string representation of an amount of dollars and cents

def dollar_format(amount):
    #returns a string representation of an amount of dollars and cents, including comma-separation of millions,thousands, and ones
    #
    #stores the number of digits before the first comma in i
    i = len(str(int(amount)))%3
    ret = "$"
    if i == 0:
        i += 3
    if amount > 1000000:
        #Checks how many commas there should be
        ret = ret + str(amount)[:i]+","+str(amount)[i:i+3]+","+str(amount)[i+3:]

    elif amount > 1000:
        ret = ret + str(amount)[:i]+","+str(amount)[i:]

    else:
        ret = ret + str(amount)
    return ret
    
###############################
print("Test Cases:")
print("dollar_format(314895030.56)= ",dollar_format(314895030.56))
print("dollar_format(31489503.56)= ",dollar_format(31489503.56))
print("dollar_format(3148950.56)= ",dollar_format(3148950.56))
print("dollar_format(314895.56)= ",dollar_format(314895.56))
print("dollar_format(31489.56)= ",dollar_format(31489.56))
print("dollar_format(3148.56)= ",dollar_format(3148.56))
print("dollar_format(314.56)= ",dollar_format(314.56))
print("dollar_format(3.56)= ",dollar_format(3.56))
