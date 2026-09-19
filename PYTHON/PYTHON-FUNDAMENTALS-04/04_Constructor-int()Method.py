# Constructor-int() Method
# The int() method returns an integer object from any number or string.
# It can be used to convert a string or a float to an integer.
# Example: Using the int() method to convert a string and a float to an integer.
# Converting a string to an integer

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)  # Convert age to integer

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the student class
student1 = student("Alice", "20")  # Passing age as a string
student1.display()  # Output: Name: Alice, Age: 20
student2 = student("Bob", 22.5)  # Passing age as a float
student2.display()  # Output: Name: Bob, Age: 22
