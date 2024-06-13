# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result  = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def sum(a,b):
    time.sleep(4)
    return a+b

print(sum(2,3))
print(sum(2,3))
print(sum(6,3))