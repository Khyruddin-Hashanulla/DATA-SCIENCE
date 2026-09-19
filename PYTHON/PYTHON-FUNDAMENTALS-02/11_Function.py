"""Function is a block of code that performs a specific task.It can take inputs, process them, and return an output.
Functions help in organizing code, making it reusable, and improving readability.
"""

# Example of a simple function that takes two numbers as input and returns their sum
# Function definition
def add_numbers(a, b): # Parameters a and b are inputs to the function
    return a + b

# Calling the function and storing the result
result = add_numbers(5, 10)
print("The sum is:", result)

# WAP to calculate the average of 3 numbers using a function
def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

# Calling the function and storing the result
avg_result = calculate_average(10, 20, 30)
print("The average is:", avg_result)
