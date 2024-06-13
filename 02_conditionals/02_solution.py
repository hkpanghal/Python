# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


# solution 1 ====> 

# age = int(input("Enter the age : "))
# day = input("Enter the day of the week in lowercase : ")

# if(day == "wednesday"):
#     if(age<=0):
#         print("Please provide valid age")
#     elif(age < 18):
#         print("Congrats it's wednesday you got discount of $2  your ticket price is $6")
#     else:
#         print("Congrats it's wednesday you got discount of $2  your ticket price is $10")
# else:
#     if(age<=0):
#         print("Please provide valid age")
#     elif(age < 18):
#         print("your ticket price is $8")
#     else:
#         print("your ticket price is $12")



# solution 2 ====> 

age = int(input("Enter the age : "))
day = input("Enter the day of the week in lowercase : ")

price = 12 if age >= 18 else 8

print("Your ticket price is $",price-2) if day == "wednesday" else print("Your ticket price is $",price)