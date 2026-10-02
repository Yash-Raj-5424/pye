#create a @debug decorator that prints function name and all its arguments for all the functions

def debug(func):
    def wrapper(*args, **kwargs):
        arg_values = ', '.join(str(arg) for arg in args)
        kwarg_values = ', '.join(f"{k}:{v}" for k,v in kwargs.items())

        print(f'fucntion {func.__name__} called with args values: {arg_values} and kwarg values: {kwarg_values}')

        return func(*args, **kwargs)

    return wrapper

@debug
def greeting(name, msg="hey"):
    print(f'{msg}! {name}')

greeting('nick', msg='hello')