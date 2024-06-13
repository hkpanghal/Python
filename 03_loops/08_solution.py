# Problem: Check if a number is prime.


num = int(input("Enter the to check prime no. or not : "))
i=2

if(num == 1):
    print("not prime no. ")
    exit()



while(i< num/2 ):
    if(num%i == 0 ):
        print("Not a prime no. ")
        exit()
    i+=1

print("prime no. ")