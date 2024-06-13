# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while(True):
    num = int(input("Enter the no. between 1 to 10 : "))
    if(num >= 1 and num <=10 ):
        print("Valid input")
        break
    else:
        print("invalid input")

