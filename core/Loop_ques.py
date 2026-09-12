# 1. count positive no. in a list

# a = [1, -2, 3, -3, 1, 3, 0, -2]
# count = 0
# for x in a:
#     if x > 0:
#         count += 1
# print(count)

# 2. sum of even numbers in a range
sum = 0
n = 10
list = [x for x in range(n) if x % 2 == 0]

# find first non-repeating character in string
s = "abxabxdtatzp"
for i in range(len(s)):
    found = 0
    for j in range(i+1, len(s)):
        if s[j] == s[i]:
            found = 1
            break
    if found == 0:
        print(s[i])
        break