"""
Q4. The user enters a string containing a number (e.g., "123"). Convert it to:
- An integer
- A float
- A string again
Print all three values and their types.
"""

num_str = input("Please Enter A String Containing A Number: ");
num_int = int(num_str);
num_float = float(num_str);
num_str_again = str(num_int);
print(f"Integer: {num_int}, Type: {type(num_int)}");
print(f"Float: {num_float}, Type: {type(num_float)}");
print(f"String: {num_str_again}, Type: {type(num_str_again)}");
