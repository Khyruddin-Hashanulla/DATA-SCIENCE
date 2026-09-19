# Class Methods in Python are methods that are bound to the class rather than its instances. They can be called on the class itself, and they have access to the class's attributes and methods. Class methods are defined using the `@classmethod` decorator and take `cls` as their first parameter, which refers to the class itself.

class Laptop:
    # Class attribute
    brand = "Dell"

    def __init__(self, model, price):
        # Instance attributes
        self.model = model
        self.price = price

    # Class method to display the brand of the laptop
    @classmethod
    def display_brand(cls):
        print(f"Brand: {cls.brand}")

# Creating instances of the Laptop class
laptop1 = Laptop("XPS 13", 1000)
laptop2 = Laptop("Inspiron 15", 800)

# Calling the class method
Laptop.display_brand()
