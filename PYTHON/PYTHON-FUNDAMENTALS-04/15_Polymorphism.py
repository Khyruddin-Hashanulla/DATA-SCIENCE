# Polymorphism in Python refers to the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.
# Function overloading and duck typing are two common ways to achieve polymorphism in Python.

# Example of polymorphism using method overriding
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example of polymorphism using duck typing
class Bird:
    def speak(self):
        return "Chirp!"

# Function that takes an animal object and calls its speak method
def animal_sound(animal):
    print(animal.speak())

# Creating instances of Dog, Cat, and Bird
dog = Dog()
cat = Cat()
bird = Bird()

# Calling the animal_sound function with different animal objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird)  # Output: Chirp!
