"""
Q3. Create a class Student with private attributes _name, _roll_number, and _marks
Provide getter and setter methods with validation (e.g marks can not be negative, roll no has to be between 1 and 100 and name cannot be empty) for each attribute.
"""

class Student:
    def __init__(self, name, roll_number, marks):
        self._name = None
        self._roll_number = None
        self._marks = None
        self.set_name(name)
        self.set_roll_number(roll_number)
        self.set_marks(marks)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name:
            self._name = name
        else:
            print("Name cannot be empty.")

    def get_roll_number(self):
        return self._roll_number

    def set_roll_number(self, roll_number):
        if 1 <= roll_number <= 100:
            self._roll_number = roll_number
        else:
            print("Roll number must be between 1 and 100.")

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative.")

# Example usage
student = Student("Alice", 25, 85)
print(f"Name: {student.get_name()}")
print(f"Roll Number: {student.get_roll_number()}")
print(f"Marks: {student.get_marks()}")
