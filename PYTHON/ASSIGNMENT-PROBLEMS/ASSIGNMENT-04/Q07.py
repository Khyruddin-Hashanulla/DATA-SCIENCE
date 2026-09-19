"""
Q7. Create a class Person that allows the constructor to work with:
- Name Only
- Name and Age
- Name, Age and Address
As direct constructor overloading(multiple constructors) are not allowed but
we have to use default parameters to simulate constructor overloading.
"""


class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        info = f"Name: {self.name}"
        if self.age is not None:
            info += f", Age: {self.age}"
        if self.address is not None:
            info += f", Address: {self.address}"
        return info

# Example usage:
person1 = Person("Alice")
person2 = Person("Bob", 30)
person3 = Person("Charlie", 25, "123 Main St")

print(person1.display_info())
print(person2.display_info())
print(person3.display_info())
