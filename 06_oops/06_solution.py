# Problem: Add a class variable to Car that keeps track of the number of cars created.


class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def display(self):
        return f'{self.brand} {self.model}'
    
    def fuel_type(self):
        return "Petrol or diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
   
tesla_car = ElectricCar("Telsa","Model S","89KWH")
my_car = Car("Tata","Safari")

print(Car.total_car)