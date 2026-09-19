"""
Q5. Create a base class Vehicle with attributes like brand and model.
Create two sub-classes Car and Bike that add extra attributes:
- Car: seats
- Bike: engine_cc
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

# Example usage
car = Car("Toyota", "Camry", 5)
bike = Bike("Yamaha", "R15", 155)
print(f"Car: {car.brand} {car.model}, Seats: {car.seats}")
print(f"Bike: {bike.brand} {bike.model}, Engine CC: {bike.engine_cc}")
