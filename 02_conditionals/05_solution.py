# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter the weather sunny , rainy or snowy : ")

if(weather == "sunny"):
    print("go for a walk")
elif(weather == "rainy"):
    print("read a book")
elif(weather == "snowy"):
    print("build a snowman")
else:
    print("can't find activity")
