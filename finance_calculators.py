# This is a Python program created to perform two financial calculations using variables and control structures.
# For investment menu, user inputs the amount, interest rate and numbers of years from which simple or compound interest 
# is calculated upon user selection.
# For bond menu, user inputs the value of the house, interest rate and number of months and then the amount to pay
# for home loan is calculated. 

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

menu = input("\nEnter either 'investment' or 'bond' form the menu above to proceed: ").lower()

if menu == "investment":
    deposit_amount = float(input("Enter the amount of money you'd like to deposit: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = float(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter either 'simple' or 'compound' interest: ").lower()
    if interest_type == "simple":
        simple_total = deposit_amount *(1 + (interest_rate/100)*years)
        print(f"Your investment will yield a return of {simple_total} through simple interest.")
    elif interest_type == "compound":
        compound_total = deposit_amount * math.pow((1+interest_rate/100),years)
        print(f"Your investment will yield a return of {compound_total} through compound interest.")

elif menu == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate2 = float(input("Enter the interest rate: "))
    num_months = float(input("Enter the number of months you plan to take to repay the bond: "))
    repayment = ((interest_rate2/100)/12 * present_value)/(1 - (1 + (interest_rate2/100)/12)**(-num_months))
    print(f"The amount of money you'll have to repay each month is {repayment}")

else:
    print("Invalid input. Please try again.")
