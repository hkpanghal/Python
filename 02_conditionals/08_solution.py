# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


password = input("Enter the password : ")

length = len(password)

if(length < 6):
    print("weak password")
elif(length <= 10):
    print("medium password")
else:
    print("strong password")