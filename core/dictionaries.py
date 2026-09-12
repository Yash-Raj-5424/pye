'''

dic = {
    0: "name",
    1: "age",
    "day": "monday",
    "month": "jan"
}

print(dic)
dic[1] = "age(yr)"
print(dic)
print(dic.get("non_existing_key", "default value"))

'''
items = {
    "one": "ONE",
    "two": "four",
    "three": "nine",
    "four": "sixteen"
}

'''
print(items)
print(items["one"])
print(f'Non existing key using .get() {items.get("five")}') # None
print(items["five"]) # KeyError

'''

'''
for key, val in items.items():
    print(f'{key}: {val}')

if "one" in items:
    print('I have \'one\' key')

'''

# pushing and popping

# items["five"] = "twenty-five"
# items.pop("four")   # remove the item with key "four"
# print(items)

# items.popitem()   # removes the latest added item
# print(items)

del items["one"]    # deletes the item from the memory

# shorthand for creating dicts
sq_nums = {x:x**2 for x in range(5)}
print(sq_nums)

keys = ["one", "two", "three", "four"]
default_val = ["squares"]

mydict = dict.fromkeys(keys, default_val) # takes each key from list and assign them default values
print(mydict)

mydict = dict.fromkeys(keys, keys) # takes keys and assigns the list as value for each of the keys
 

 ## USe a dictionary to count he frequency of elements in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)


## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2} # The ** operator expands dict1 into individual key-value pairs inside the new dictionary {} and then b's value gets orverwritten from dict2
print(merged_dict)  # output: {'a': 1, 'b': 3, 'c': 4}
