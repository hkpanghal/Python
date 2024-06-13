# value = 100  #global scope


# def change():
#     value = 85 #loccal scope
#     print(value)

# change()
# print(value)


# value = 100  #global scope


# def change():
#     global value
#     value = 85
#     print(value)

# change()
# print(value)

value = 100  #global scope


def change():
    # value = 85
    def run():
        print(value)
    run()

change()
print(value)



