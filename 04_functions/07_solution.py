# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):

    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))