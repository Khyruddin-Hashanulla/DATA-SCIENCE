# List Comprehension
# List comprehension is a concise way to create lists in Python.
# It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering items based on a condition.

# Basic syntax: [expression for item in iterable if condition]

# Example 1: Creating a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9:", squares)

# Example 2: Creating a list of even numbers from 0 to 19
even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers from 0 to 19:", even_numbers)

# Example 3: Creating a list of uppercase letters from a string
input_string = "hello world"
uppercase_letters = [char.upper() for char in input_string if char.isalpha()]
print("Uppercase letters from the string:", uppercase_letters)

# Example 4: Creating a list of tuples (number, square) for numbers from 0 to 9
number_square_tuples = [(x, x**2) for x in range(10)]
print("Tuples of (number, square) from 0 to 9:", number_square_tuples)
