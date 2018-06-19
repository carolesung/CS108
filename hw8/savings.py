#File: savings.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw8 Part1
#Date: Feb 13 2018
#Description: Calculates user's balance accumulated in years

def print_savings_accumulation(rm, amount):
    #Prints out user's accumulated balance in a year as a table
    interestTTL = 0
    balance = 0
    savings = 0
    print("Savings Schedule for Year1:")
    print("month\tinterest\tamount\t\tbalance")
    for month in range(1,13):
        #Calculate the amount of interest earned on the prev balance
        interest = balance*rm
        interestTTL += interest
        #update the balance
        balance += interest + amount
        savings += amount
        print(month,"\t$%10.2f \t$%10.2f \t$%10.2f"%(interest,amount,balance))
 
    print("\nSavings summary for year 1")
    print("Total amount saved\t: $%0.2f" %savings)
    print("Total interest earned\t: $%0.2f" %interestTTL)
    print("End of year balance\t: $%0.2f" %balance)



def print_multiyear_savings_accumulation(rm, amount, years):
    #Prints total accumulated balance for multiple years
    balanceTTL = 0
    for yr in range(1, years + 1):
        print("\nSavings Schedule for Year",yr,":")
        print("month\tinterest\tamount\t\tbalance")
        balance = 0
        savings = 0
        interestTTL= 0
        for month in range(1,13):
            #Calculate the amount of interest earned on the prev balance
            interest = balanceTTL*rm
            interestTTL += interest
            #update the balance
            balanceTTL += interest + amount
            balance += interest + amount
            savings += amount
            print(month,"\t$%10.2f \t$%10.2f \t$%10.2f"%(interest,amount,balanceTTL)) 
        print("\nSavings summary for year",yr)
        print("Total amount saved\t: $%0.2f" %savings)
        print("Total interest earned\t: $%0.2f" %interestTTL)
        print("End of year balance\t: $%0.2f" %balanceTTL)
        print("*"*55)

def main():
    #Interactive program that prompts user for inputs
    print("Welcome to the savings plan calculator!")
    print("\n")
    savingsGoal = float(input("Enter your savings goal in dollars: "))
    rm = float(input("Enter the expected annual rate of return in percent (i.e. 7.5): "))
    yrs = int(input("Enter time until goal in years: "))
    rm = rm/1200
    amount = (rm*savingsGoal)/(((1+rm)**(yrs*12))-1)
    print(amount)
    print_multiyear_savings_accumulation(rm, amount, yrs)
    
main()
