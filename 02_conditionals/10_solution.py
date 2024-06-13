# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_name = input("Enter the pet's name or species : ")
pet_age = int(input("Enter the pet's age : "))

if(pet_age < 2):
    print("puppy food")
else:
    print("senior",pet_name,"food")
