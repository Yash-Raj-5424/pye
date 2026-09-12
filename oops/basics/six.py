class B:
    paisa = 92
    def __init__(self, profit):
        self.profit = profit

    # @staticmethod
    def greet(self, message):
        print(message)
    
    @classmethod
    def create_default(cls):
        return cls.paisa

b = B(11) 
a = B(234)
print(a.profit)           
print(B.create_default())
print(b.paisa)

obj = B(55)
obj.greet("kay kay")