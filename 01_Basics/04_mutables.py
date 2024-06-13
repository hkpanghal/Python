# In Python, objects are categorized as mutable and immutable based on whether their values can be changed after creation. Mutable objects can be modified in place, while immutable objects cannot be altered once they are created.
# Mutable objects in Python include:

# lists, dictionaries, and sets.


# Python Lists are just like dynamic-sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it the most powerful tool in Python.
mylist = [1,2,3]

mylist.append(4)
mylist[1] = 5

# print(mylist)

dataList = [1,2,3]
copyList = dataList
dataList[1] = 5

# print(dataList,copyList)

dataList = [1,2,3]
copyList = dataList.copy() # returns shallow copy
dataList[1] = 5

# print(dataList,copyList)

dataList = [1,2,3,[5,6,7]]
copyList = dataList.copy() # returns shallow copy
dataList[3][0] = 10

# print(dataList,copyList)

# ====================================================================================================
# Dictionary in Python is an ordered (since Py 3.7) [unordered (Py 3.6 & prior)] collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.


myDict = {"name":"Sahil","age":29,"country":"Bharat"}

myDict["age"] = 40

# print(myDict)

dataDict = {"name":"Jhon","age":39,"country":"USA"}
copyDict = dataDict

dataDict["age"] = 45
# print(dataDict,copyDict)

dataDict = {"name":"Jhon","age":39,"country":"USA"}
copyDict = dataDict.copy() # returns shallow copy 

copyDict["age"] = 45
# print(dataDict,copyDict)

dataDict = {"name":{"firstName":"Rahul","lastName":"Kumar"},"age":39,"country":"USA"}
copyDict = dataDict.copy() # returns shallow copy 

copyDict["name"]["firstName"] = "Sahil"
# print(dataDict,copyDict)

# ====================================================================================================
# A Python Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set.


mySet = {1,2,3}
mySet = {4,5,"Hello",5}
mySet.add(6)
# print(mySet)
# print(mySet)

dataSet = {10,9,8}
copySet = dataSet
copySet.add(5)

# print(dataSet,copySet)

dataSet = {10,9,8}
copySet = dataSet.copy() # returns shallow copy
copySet.add(5)

# print(dataSet,copySet)


