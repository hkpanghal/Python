
def power(pow):
    def calculate(num):
        print( num ** pow)
    
    return calculate

calculate = power(3)

calculate(3)
calculate(4)
calculate(5)
