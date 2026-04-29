"""
Calculator backend module
"""
def func():
    pass

def display_header_menu():
    """
    Displays the header menu for calculator
    """
    print("This is a calculator menu".center(100, "-"))
    print("1.Add".ljust(100))
    print("2.Sub".ljust(100))
    print("3.Mul".ljust(100))
    print("4.Div".ljust(100))
    print("5.Quit".ljust(100))
    print("-"*100)

def add(a: int,b: int) -> int:
    """
    Adds two numbers and returns its sum
    """
    return a+b

def sub(a: int,b: int) -> int:
    """
    Subtracts two Numbers and returns its difference
    """
    return a - b 

def mul(a,b):
    pass

def div(a,b):
    return b != 0 and a / b
    
# k = display_header_menu()
# print(k)

if __name__ == '__main__':
    while True:
        display_header_menu()
        choice = input("Enter the choice: ")
        if choice == "1":
            numbers = tuple(map(int, input("Enter 2 numbers seperated by space(' '): ").split()))
            total = add(*numbers) # Passing the values
            print(f"Sum of {numbers[0]} and {numbers[1]} is: {total}")
        elif choice == "2":
            numbers = list(map(int, input("Enter 2 numbers seperated by space(' '): ").split()))
            total = sub(numbers[0], numbers[1])
            print(f"Difference of {numbers[0]} and {numbers[1]} is: {total}")
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("Quitting.....")
            break
        else:
            print("Invalid Choice")