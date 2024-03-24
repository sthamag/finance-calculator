# This is a Python program created to perform two financial calculations using variables and control structures.
# For investment menu, user inputs the amount, interest rate and numbers of years from which simple or compound interest 
# is calculated upon user selection.
# For bond menu, user inputs the value of the house, interest rate and number of months and then the amount to pay
# for home loan is calculated. 

import math

# Display menu options
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Get user's choice from the menu
menu = input("\nEnter either 'investment' or 'bond' form the menu above to proceed: ").lower()

# Handle investment calculation
if menu == "investment":
    try:
        # Get inputs from the user
        deposit_amount = float(input("Enter the amount of money you'd like to deposit: "))
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        
        interest_rate = float(input("Enter the interest rate (as a percentage): "))
        if interest_rate <= 0:
            raise ValueError("Interest rate must be a positive number.")
        
        years = float(input("Enter the number of years you plan to invest: "))
        if years <= 0:
            raise ValueError("Number of years must be a positive number.")
        
        interest_type = input("Enter either 'simple' or 'compound' interest: ").lower()
        if interest_type not in ["simple", "compound"]:
            raise ValueError("Invalid interest type. Please enter either 'simple' or 'compound'.")

        # Calculate investment return based on the user's inputs
        if interest_type == "simple":
            simple_total = deposit_amount *(1 + (interest_rate/100)*years)
            print(f"Your investment will yield a return of {round(simple_total, 2)} through simple interest.")
        elif interest_type == "compound":
            compound_total = deposit_amount * math.pow((1+interest_rate/100),years)
            print(f"Your investment will yield a return of {round(compound_total, 2)} through compound interest.")
    
    except ValueError as e:
        # Handle invalid inputs
        print("Invalid input:", e)

# Handle bond calculation
elif menu == "bond":
    try:
        # Get inputs from the user
        present_value = float(input("Enter the present value of the house: "))
        if present_value <= 0:
            raise ValueError("Present value must be a positive number.")
        
        interest_rate2 = float(input("Enter the interest rate: "))
        if interest_rate2 <= 0:
            raise ValueError("Interest rate must be a positive number.")
        
        num_months = float(input("Enter the number of months you plan to take to repay the bond: "))
        if num_months <= 0:
            raise ValueError("Number of months must be a positive number.")
        
        # Calculate bond repayments based on the user's inputs
        repayment = ((interest_rate2/100)/12 * present_value)/(1 - (1 + (interest_rate2/100)/12)**(-num_months))
        print(f"The amount of money you'll have to repay each month is {round(repayment, 2)}")
    
    except ValueError as e:
        # Handle invalid inputs
        print("Invalid input:", e)

# Handle invalid menu choice
else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")
