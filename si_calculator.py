# This is a comment, It is not processed by interpreter
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate the simple interest
# si = ptr / 100


principal = 300000
time_in_months =36
rate_of_interest = 0.07

simple_interest = (principal * time_in_months * rate_of_interest) / 100

# print(simple_interest)
# print("The simple interest is:",   simple_interest)
# print("The simple interest is:" + str(simple_interest))
# print("The simple interest is: %.2f"%simple_interest)
# print("The simple interest of {0} at {1:.2f}% for {2} months is: {3:.2f}".format(principal, rate_of_interest * 100, time_in_months, simple_interest))
print(f"The simple interest of {principal} at {rate_of_interest * 100:.2f}% for {time_in_months} months is: {simple_interest:.2f}")


