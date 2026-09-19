"""
Finally Keyword in Python - The `finally` keyword in Python is used in exception handling to define a block of code that will always be executed,
regardless of whether an exception was raised or not. This is useful for cleaning up resources, such as closing files or releasing locks, that need to be done no matter what happens in the try-except blocks.
"""

try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
finally:
    print("Execution of the try-except block is complete. This message will always be printed.")
