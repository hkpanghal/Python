# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Enter the distance : "))

if(distance <= 0 or distance > 15):
    print("can't find mode of transportation")
elif(distance < 3):
    print("walk")
elif(distance < 15):
    print("bike")
else:
    print("car")
