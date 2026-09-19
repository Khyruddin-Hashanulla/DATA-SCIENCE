# Inheritance in Python is a fundamental concept in object-oriented programming that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and establishes a hierarchical relationship between classes.

# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.doors = doors

    def honk(self):
        print(f"{self.brand} {self.model} honks: Beep Beep!")

# Creating an instance of Car
my_car = Car("Toyota", "Camry", 4)

# Accessing methods from both the parent and child classes
my_car.start_engine()  # Toyota Camry's engine started.
my_car.honk()  # Toyota Camry honks: Beep Beep!
