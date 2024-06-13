# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# sloution 1 ==== >

# age = int(input("Enter the age of person : "))

# if(age <= 0 ):
#     print("Invalid age")
# elif(age <13):
#     print("Person is child ")
# elif(age>=13 and age <=19):
#     print( "Person is teenager")	
# elif(age>=20 and age <=59):
#     print("Person is adult")
# else:
#     print("Person is senior")


# sloution 2 ==== >

age = int(input("Enter the age of person : "))

if(age <= 0 ):
    print("Invalid age")
elif(age <13):
    print("Person is child ")
elif( age <19):
    print( "Person is teenager")	
elif(age < 60):
    print("Person is adult")
else:
    print("Person is senior")