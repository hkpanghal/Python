# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def display(self):
        return f'{self.brand} {self.model}'
    
    def get_brand(self):
        return self.__brand

my_car = Car("Tata","Safari")

print(my_car.get_brand())