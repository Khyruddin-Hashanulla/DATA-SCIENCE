"""
Q9. Create the following classes: Harbivore, Carnivore, Omnivore with some attributes and methods.
Then create a class Bear that inherits from all above classes to showcase how multiple inheritance works in Python.
"""

class Harbivore:
    def __init__(self, name):
        self.name = name

    def eat_plants(self):
        return f"{self.name} is eating plants."

class Carnivore:
    def __init__(self, name):
        self.name = name

    def eat_meat(self):
        return f"{self.name} is eating meat."

class Omnivore:
    def __init__(self, name):
        self.name = name

    def eat_both(self):
        return f"{self.name} is eating both plants and meat."

class Bear(Harbivore, Carnivore, Omnivore):
    def __init__(self, name):
        super().__init__(name)

# Example usage
bear = Bear("Grizzly")
print(bear.eat_plants())  # Output: Grizzly is eating plants.
print(bear.eat_meat())    # Output: Grizzly is eating meat.
print(bear.eat_both())    # Output: Grizzly is eating both plants and meat.
