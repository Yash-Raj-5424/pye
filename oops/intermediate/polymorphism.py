class Parent:
    def __init__(self, username, salary):
        self.username = username
        self.salary = salary
    
    def greet(self):
        return "hello parent"

class Child(Parent):
    def __init__(self, username, salary):
        super().__init__(username, salary)
    
    def greet(self):
        return "hello child"


p = Parent("Jack", 120)
c = Child("Josh", 110)
print(p.greet())
print(c.greet())