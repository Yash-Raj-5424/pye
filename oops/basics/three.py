class T:
    a = 234

t = T()
print(t.a) # class level value of a => 234

t.a = 111
print(t.a)

t.a = "adtwet5"
print(t.a)
print(T.a)

p = T()
print(p.a)
p.a = 2222
print(p.a)
