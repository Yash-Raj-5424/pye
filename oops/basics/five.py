class B:
    def __init__(self, *args):
        if len(args) == 0:
            print("no arguments")
        elif len(args) == 1:
            print(f"one arg: {args[0]}")
        else:
            print(f"multiple args: {args}")

b = B()              
a = B(234)           
c = B(1, 2, 3)       