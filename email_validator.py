# just check presence of '@' in the string
email = input("Enter email id: ")
if email.find('@') == -1:
    print("Invalid Email")
else:
    print("Valid Email")
