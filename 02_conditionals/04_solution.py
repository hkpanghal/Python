
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter the fruit name : ")
color = input("Enter the fruit color : ")


if(color == "green"):
    print(fruit,"is unripe")
elif(color == "yellow"):
    print(fruit,"is ripe")
elif(color == "brown"):
    print(fruit,"is overripe")
else:
    print("can't predict")