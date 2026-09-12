class A:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def greet(self):
        return f"Hello {self.name}"

class Child(A):     #inherits from A
    def __init__(self, name, roll, marks):
        super().__init__(name, roll)  #set the values in constructor of parent class
        self.marks = marks

obj = A("Jack", 12)
print(obj.name)
print(obj.greet())

obj2 = Child("Josh", 12, 98)
print(obj2.name)
print(obj2.greet())