# Immutable objects in Python include:
# Strings, Integers, Floats, Tuples, Booleans, and Frozensets.

name = "Rahul"
# name[1] = "S" TypeError: 'str' object does not support item assignment
# print(name)

name = "Sahul"
# print(name)

myInt = 4
myFloat = 4.4

myBool = True

# =================================================================================================================

# The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
mylist = ["apple","banana","1",1]
fset = frozenset(mylist)
# fset[0] = "cherry" TypeError: 'frozenset' object does not support item assignment


# print(mylist,fset)

# =================================================================================================================
# A tuple is a collection which is ordered and unchangeable.

myTuple = ("Rahul",1,2,1,"Banana",5.2)

# print(myTuple[0])

# myTuple[0] = "Sahil" TypeError: 'tuple' object does not support item assignment