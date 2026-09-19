# Attributes and Methods in Python
"""
- Attributes are variables that belong to an object
- Methods are functions that belong to an object
Example: Creating a simple class with attributes and methods.
"""
class Student:
    subject = "Mathematics"  # Class attribute shared by all instances

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating instances of the Student class
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

# Accessing attributes and methods of the instances
print(f"Student 1: {s1.name}, Age: {s1.age}, Subject: {s1.subject}")
print(f"Student 2: {s2.name}, Age: {s2.age}, Subject: {s2.subject}")
print(s1.introduce())
print(s2.introduce())
