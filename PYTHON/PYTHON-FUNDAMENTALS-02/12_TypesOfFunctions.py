# Types of Functions in Python
# 1. Built-in Functions: These are functions that are already defined in Python and can be used directly without any additional code. Examples include print(), len(), type(), etc.
# 2. User-defined Functions: These are functions that are defined by the user to perform specific tasks. They are created using the def keyword followed by the function name and parentheses.
# 3. Anonymous Functions (Lambda Functions): These are small, unnamed functions defined using the lambda keyword

# Example: Built-in Function
# Using the built-in len() function to find the length of a string
my_string = "Hello, World!"
length = len(my_string)
print("The length of the string is:", length)

# Example: User-defined Function
# Function to calculate the square of a number
def square(num):
    return num * num

# Calling the user-defined function
result = square(5)
print("The square of 5 is:", result)

# Example: Anonymous Function (Lambda Function)
# Using a lambda function to calculate the cube of a number
cube = lambda x: x ** 3
# Calling the lambda function
result = cube(3)
print("The cube of 3 is:", result)
