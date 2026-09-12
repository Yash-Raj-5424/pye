# chars = ['a', 'b', 'c', 'd']
# print(chars.index('jack')) # ValueError 'jack' doesn't exist

a = [1, 2, 3, 4, [5, 6, 7]]

'''
# reference assignment

print(f'a before change: {a}')
b = a # reference assignment i.e,. both b & a point to the same object
print(f'b before change: {b}')
b[0] = 2    # both original and copy will get changed
print(f'a after change: {a}\n')

'''

'''
# shallow copy -> creates a new container (the outer [])
# but copies references to nested objects - inner []s

c = a.copy()    # creates a shallow copy
print(f'a before change: {a}')
c[0] = 8    # doesn't change original list
print(f'a after top level change by c: {a}') # a stays the same
b[4][0] = 200   # nested level change modifies both a & b
print(f'a after nested level change by c: {a}')
'''

'''
# deep copy of lists - no effect on original at all

import copy

d = copy.deepcopy(a)
print(f'\nDeep copy of a -> d = {d}')
d[0] = 100  # won't affect a
print(f'a after top level change by deep copy: {a}')
d[4][0] = 500   # will not affect a
print(f'a after nested level change by deep copy: {a}')

'''

'''
# copying a list using slicing
x = [1, 2, 3, 4]
y = x # this is reference assignment
p = x[:] # it creates a copy i.e new object in the memory

x[0] = 22
print(f'x: {x}')
print(f'p: {p}')
p[1] = 55 # p points to a new object and the change reflects only in that
print(f'x: {x}')    # x is unaffected by p's change
print(f'p: {p}')

'''

# some extra functions of lists
# print(c.sort()) # prints None as sort() doesn't return anything
# print(c)    # prints the sorted list

# append(item) -> appends to the end
# extend(iterable) -> appends all items of the iterable
# insert(i, item)
# remove(item)
# pop() -> pop last item
# pop(i) -> remove at item at i

# some other operations on lists

# x = ["abc", "def", "pqqr", "mno"]
# x[1] = "yes"
# print(x)
          
# # x[1: 2] = "hello"   # separately stored as h, e, l, l, o
# # print(x)

# x[1: 2] = ["hello"] # now it is treated as "hello"
# print(x)

# x[1: 4] = ["val1", "val2", "val3"] # replace values at index 1, 2, 3
# print(x)

# x[0] = []   # it inserts an [] at this index
# print(x)

ls = ["asdf", "masdfh", "adfw", "werews"]
ls[1:1] = ["hello"] # this inserts "hello" at index 1 and others shift to right
# we can use insert(index, item) also
print(ls)

ls[1: 2] = [] # removes the item at index 1
print(ls)
