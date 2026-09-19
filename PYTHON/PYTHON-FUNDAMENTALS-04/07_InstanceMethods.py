# Instance methods in Python are functions that are defined within a class and are used to perform operations on instances of that class. They have access to the instance's attributes and can modify them. Instance methods are defined using the `def` keyword and take `self` as their first parameter, which refers to the instance itself.

class Student:
    # Class attribute
    school_name = "ABC High School"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method to display student details
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

# Creating instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Calling the instance method
student1.display_details()
student2.display_details()
