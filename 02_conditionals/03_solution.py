# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


score = int(input("Enter the student score : "))

if(score < 60):
    print("Student grade is F")
elif(score <= 69):
    print("Student grade is D")
elif(score <= 79):
    print("Student grade is C")
elif(score <= 89):
    print("Student grade is B")
elif(score <= 100):
    print("Student grade is A")
else:
    print("Marks are greater than 100")