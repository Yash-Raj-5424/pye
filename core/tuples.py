'''
tup = (1, 3, 234) # tuples are immutable
print(tup)

# tup[1] = 64 # TypeError
print(tup)

# we can create list of tuples
list_of_tup = [(1, 2), (4, 1, 1, 4, 6)]
list_of_tup[0] = 2  # works fine -> list is mutable
print(list_of_tup)               
'''

# small1 = (1, 2, 3)
# small2 = (4, 5, 6)
# large = small1 + small2

# print(large) # would merge both the tuples

# nums = (1, 2, 3)
# repeated_thrice = nums*3
# print(repeated_thrice)

#packing and unpacking in tuples
# packed = 1, 2, 3, 'a', "yes", 3.14
# print(packed)   #creates a tuple

# a, b, c, d, e, f = packed   #all receive the values in the order
# print(a, b, c, d, e, f)

# unpacking using * catcher
# a, *others, c = packed

# print(a, others, c) #others will pack all the elems in a list except 1st and last

# print(a, *others, c) # *others again unpacks

# nested tuples
x = ((1, 2, 3), (10, 20, 30), ('a', 'b', 'c'))

# iterating a nested tuple - just fun
for sub_tup in x:
    print('tuple => ', '(', end='', )
    for item in sub_tup:
        print(item, end=', ')
    print(')' , end='')
    print()