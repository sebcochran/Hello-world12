"""
Name: Sebastian Cochran 
Version(ID): D
Program: Quiz1D_SEBCOCHRAN.py

Purpose: Calculate the monthly morgage payment for a loan rounded to
1. Signify Constants
    monthly payment 
2. the inputs are 
    Principal amount 
    Annual interest rate 
    Number of loans taken
2. Computations 
    Monthly Payment = (p * r / 1200) * (1/ (1 - (1 + r / 1200)) ** (-12 * t)))
3. Outputs are 
    Monthly Payment 
"""

# defining monthly payment 


# Enter the inputs 
p = float(input("Enter the Principal Amount: "))
r = float(input("Enter the annual interest rate: "))
t = float(input("Enter the time period(in years): "))

# Compute the monthly income 
monthly_payment = p * r / 1200 * 1 / (1 - (1 + r / 1200) ** (-12 * t))

# Print the Monthly Payment
print("The monthly payment is: $" + str(round(monthly_payment,2)))

