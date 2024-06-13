# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    def display(self):
        return f'{self.brand} {self.__model}'
    
    def get_brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model

my_car = Car("Tata","Safari")

print(my_car.model)