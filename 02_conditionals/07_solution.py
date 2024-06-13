# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter the order size small , medium , large : ")
extra_shot = input("Do you want extra show type 'y' for yes or 'n' for no : ")

if(extra_shot == 'y'):
    print(order_size,"coffee with Extra shot")
else:
    print(order_size,"coffee")