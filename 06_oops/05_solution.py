# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.



class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

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

print(tesla_car.fuel_type(),"\n" ,my_car.fuel_type())