"""
Author: Vishwas Singh
Email: vishwas@cloudthat.com
Script to calculate the sum of n numbers
"""
n = 0
total = 0
count = 0
while True:
    n = input("enter the number or q to stop: ")
    if n == 'q':
        break
    n = int(n)
    total += n
    count += 1

print(f"The sum of {count} numbers is: {total} & \naverage is: {total/count}")
