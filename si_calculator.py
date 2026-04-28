"""
Author: Vishwas K Singh
Email: vishwas@cloudthat.com
Script to calculate the simple interest
si = ptr / 100
"""

principal = float(input("Enter the Principal amount: "))
time_in_months = int(input("Enter the time in months: "))
rate_of_interest = float(input("Enter the rate of interest: "))

simple_interest = (principal * time_in_months * rate_of_interest) / 100

print(f"The simple interest of {principal} at {rate_of_interest * 100:.2f}% for {time_in_months} months is: {simple_interest:.2f}")