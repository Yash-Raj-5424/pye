x = 10
y = x   # y points to the memory ref of x
print(x)
print(y)
x = 15  # now x points to a new object with value 15
print(y) # y still points to the earlier ref but x is now pointing to 15