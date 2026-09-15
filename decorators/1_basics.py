# WKT functions in python are first-class objs i.e, it can be passed as args, assigned to vars and returned from other funcs just like other vars
# A Decorator is simply a wrapper or more technically a higher-order-function that takes an original function as an input, wraps it inside an inner function with some extra code and returns that inner wrapper function

# Example:

def my_decorator(original_func):
    def wrapper():
        print('do something here')
        original_func()     # call the original function
        print('something happens after original function is called')

    return wrapper

# apply the decorator using '@' symbol

@my_decorator
def any_fucntion():
    print("this is any function")

# call the function
any_fucntion()  # any_function will be passed to my_decorator and will be executed inside the wrapper function there