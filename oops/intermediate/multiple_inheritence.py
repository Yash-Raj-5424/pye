class Parent_One:
    def greet(self):
        print("parent one")

class Parent_Two:
    def greet(self):
        print("parent two")

class Child(Parent_Two, Parent_One):
    pass

c = Child()
c.greet()