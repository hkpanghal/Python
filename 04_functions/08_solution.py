# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.



def format(**kwargs):

    for key,value in kwargs.items():
        print(f"{key} : {value}")


format(name="shaktiman",power="spin")
format(power="spin",name="shaktiman")
format(power="spin",name="shaktiman",enemy="Jackaal")



