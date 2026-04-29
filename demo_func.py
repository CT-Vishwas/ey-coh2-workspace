# Scope of variables
m = 100

def add(a,b):
    # global m
    # print(f"value of m inside add is {m}") # Gives Error because m is defined below
    m = 25
    print(f"value of m inside add is {m}")
    return a + b

def func():
    pass

print(f"L13: value of m outside add is {m}")
add(23,45)
print(f"L15: value of m outside add is {m}")
