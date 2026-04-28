# valid Email

email = input("Enter the email id: ")
if email.find("@") != -1:
    uname = email[:email.find("@")]
    print(f"The username extracted from email: {email} id is {uname}")
else:
    print("Invalid Email")