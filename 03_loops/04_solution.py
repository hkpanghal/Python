# Problem: Reverse a string using a loop


# str = 'hello'

# i = 0;
# j = len(str) - 1

# print(str)

# while(i<j):
#     temp = str[i]
#     str[i] = str[j]
#     str[j] = temp
#     i+=1
#     j-=1

# print(str)

str = 'hello'
revstr = ''
j = len(str) - 1
while(j>=0):
    revstr+=str[j]
    j-=1

print(revstr)