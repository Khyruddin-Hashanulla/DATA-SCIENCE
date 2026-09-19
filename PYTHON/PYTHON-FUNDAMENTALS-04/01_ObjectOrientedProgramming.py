# Object-Oriented Programming in Python
# Using classes and objects to model real-world entities and their behaviors.
# Example: Creating a simple class to represent a car.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
