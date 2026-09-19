# Type Conversion and Casting
# Type conversion is the process of converting one data type to another. In Python, this can be done using built-in functions like int(), float(), str(), etc.

# Example of type conversion
x = 5          # Integer
y = 2.5        # Float

# Converting float to integer
z = int(y)     # z will be 2
print("Value of z after converting y to int: ", z)  # Output: 2

# Converting integer to float
w = float(x)   # w will be 5.0
print("Value of w after converting x to float: ", w)  # Output: 5.0

# Casting is a way to explicitly convert a variable from one type to another. In Python, this can be done using the same functions as type conversion.

# Example of casting
a = "10"       # String
b = int(a)     # Casting string to integer
print("Value of b after casting a to int: ", b)  # Output: 10
