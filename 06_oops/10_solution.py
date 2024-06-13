# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine"
    

class ElectricCar(Battery,Engine):
    def car_info(self):
        return "This is electric car"

my_car = ElectricCar()

print(my_car.battery_info())
print(my_car.engine_info())
print(my_car.car_info())