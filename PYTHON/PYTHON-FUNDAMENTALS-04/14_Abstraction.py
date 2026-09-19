# Abstraction in Python is a concept that allows you to hide the implementation details of a class and expose only the essential features to the user. It helps in reducing complexity and increasing efficiency by providing a clear interface for interacting with objects.

from abc import ABC, ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow! Meow!"

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.make_sound())
print(cat.make_sound())
