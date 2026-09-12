try:
    num = int(input("Enter a num: "))
    res = 20 / num
except ValueError:
    print("invalid input\n")
except ZeroDivisionError as e:
    print(e, "\n")
finally:
    print("this executes anyway")