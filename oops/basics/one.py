class S:
    val = "declared in class"
    def __init__(self, val):
        self.val = val

print(S.val)
S.val = "changed using S.name"  # changes the val at class level
print(S.val)

S.othervariable = 134
print(S.othervariable)

a = S(3424)
print(a.val)

S.val = "changed again"
s = S("arg name")
print(s.val)
print(S.val)