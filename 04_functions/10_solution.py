# Problem: Create a recursive function to calculate the factorial of a number.


def fact(num):
    if(num == 1 or num == 0):
        return 1
    
    res = num * fact(num-1)

    return res


print(fact(5))

