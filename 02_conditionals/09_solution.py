# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).


year = int(input("Enter the year : "))

if(year%4 == 0 and year%100 != 0):
    print("leap year")
elif(year% 400 == 0):
    print("leap year")
else:
    print("not leap year")