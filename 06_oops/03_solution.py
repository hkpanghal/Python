# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        return f'{self.brand} {self.model}'
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size

   
tesla_car = ElectricCar("Telsa","Model S","89KWH")

print(tesla_car.model,tesla_car.brand,tesla_car.battery_size)
print(tesla_car.display())