# Factorial of a number using function in for loop

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
number = int(input("Enter a number to calculate its factorial: "))
# Calling the factorial function and storing the result
fact = factorial(number)
# Displaying the result
print(f"The factorial of {number} is: {fact}")
