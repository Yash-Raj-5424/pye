class A:
    def greet(self):
        print("greeting by A")
    def any():
        print("universe+")
    


print(A)
print(A.greet)

a = A()
print(a)
a.greet()
print("----------\n")
print(a.greet)
print(a.greet())

# o = A()
# o.any()   # here, it acts as A.any(o) since A expects 0 args and u're passing o so it gives error
