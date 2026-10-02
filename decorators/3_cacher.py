# create a decorator that caches the values from function calls

import time

def cache(func):
    cache_store = {}
    print(cache_store)
    
    def wrapper(*args):
        if args in cache_store:
            return cache_store[args]
        res = func(*args)
        cache_store[args] = res

        return res
    return wrapper


@cache
def my_func(a, b):
    time.sleep(5)
    return a+b

print(my_func(2, 4))
print(my_func(2, 4))