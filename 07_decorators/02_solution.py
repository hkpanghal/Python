# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args,**kwargs):
        print(f"calling {func.__name__} with args {[str(arg) for arg in args]} and kwargs {[f"{k} = {v}" for k,v in kwargs.items()]}")
        return func(*args,**kwargs)
    return wrapper


@debug
def hello():
    print("hello")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting} {name} !")

greet("Rahul",greeting="Hanji")
hello()