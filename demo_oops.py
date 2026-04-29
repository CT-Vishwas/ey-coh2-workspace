class Person:
    def __init__(self, uname, city):
        self.uname = uname
        self.city = city

class User(Person):
    def __init__(self, uname, city, salary):
        super().__init__(uname, city)
        self.salary = salary

p1 = Person("vishwas", "Mysore")
p2 = User("Vish","mys",20000)
print(f"The object p1 is: {p1.uname}")
print(f"The object p2 is: {p2.uname}")