class Test:
    steps = 0
    def __init__(self, money):
        self.__money = money
        Test.steps += 1
    
    @staticmethod
    def greet():
        return "hello from static method"

    @property   # makes the fields read-only and can be acccessed just by property (no method call using () )
    def money(self):
        return self.__money

t = Test(2323)
print(Test.steps)
print(t.steps)  # class variables are accessible both by obj and class

print(Test.greet())
print(t.greet())    # obj can't access static methods

print(t.money)  # no need to call money() as money is @property