# Classes and Objects in Python
"""
- A class is a blueprint for creating objects, and an object is an instance of a class
- Objects can have attributes (data) and methods (functions) that define their behavior
Example: Creating a simple class to represent a person.
"""
class Student:
    subject = "Mathematics"  # Class attribute shared by all instances:

s1 = Student()  # Creating an instance of the Student class
s1.name = "Alice"  # Adding an instance attribute to s1
s1.age = 20  # Adding another instance attribute to s1
s2 = Student()  # Creating another instance of the Student class
s2.name = "Bob"  # Adding an instance attribute to s2
s2.age = 22  # Adding another instance attribute to s2

# Accessing attributes and methods of the instances
print(f"Student 1: {s1.name}, Age: {s1.age}, Subject: {s1.subject}")
print(f"Student 2: {s2.name}, Age: {s2.age}, Subject: {s2.subject}")
