# Types of Constructors in Python
"""
- A constructor is a special method in Python classes that is automatically called when an object is created.
- There are three types of constructors in Python:
    1. Default Constructor: A constructor that takes no arguments and initializes the object with default values.
    2. Parameterized Constructor: A constructor that takes arguments to initialize the object with specific values.
    3. Copy Constructor: A constructor that creates a new object as a copy of an existing object.
"""

class Student:
    # Default Constructor
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

    # Parameterized Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Copy Constructor
    def __init__(self, student):
        self.name = student.name
        self.age = student.age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object using the default constructor
student1 = Student()  # Default constructor is called
student1.display()  # Output: Name: Unknown, Age: 0

# Creating an object using the parameterized constructor
student2 = Student("Alice", 20)  # Parameterized constructor is called
student2.display()  # Output: Name: Alice, Age: 20

# Creating an object using the copy constructor
student3 = Student(student2)  # Copy constructor is called
student3.display()  # Output: Name: Alice, Age: 20
