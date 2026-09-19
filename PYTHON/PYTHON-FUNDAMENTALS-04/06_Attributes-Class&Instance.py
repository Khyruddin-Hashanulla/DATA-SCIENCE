# Attributes in Python are variables that belong to a class or an instance of a class. They can be used to store data and define the properties of objects created from the class. There are two main types of attributes: class attributes and instance attributes.

class Student:
    # Class attribute
    school_name = "ABC High School"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Creating instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Accessing class attribute
print(f"School Name: {Student.school_name}")  # Output: School Name: ABC High School

# Accessing instance attributes
print(f"Student 1: {student1.name}, Age: {student1.age}")
print(f"Student 2: {student2.name}, Age: {student2.age}")
