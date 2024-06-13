# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        return f'{self.brand} {self.model}'
my_car = Car("Tata","Safari")

print(my_car.display())