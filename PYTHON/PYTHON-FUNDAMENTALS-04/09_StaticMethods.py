# Static Methods in Python
# Static methods in Python are methods that belong to a class but do not have access to the instance or class attributes. They are defined using the `@staticmethod` decorator and do not take `self` or `cls` as their first parameter. Static methods are used for utility functions that perform a task in isolation.

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
result1 = Calculator.add(5, 3)
result2 = Calculator.multiply(4, 6)

print(f"Addition: {result1}")  # Output: Addition: 8
print(f"Multiplication: {result2}")  # Output: Multiplication: 24
