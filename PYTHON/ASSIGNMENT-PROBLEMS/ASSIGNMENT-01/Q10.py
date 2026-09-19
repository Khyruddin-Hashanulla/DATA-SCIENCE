"""
Q10. Take a Decimal number as input (like 3.14) from the user and output its:
- Integer part - 3
- Fractional part - 0.14
"""

# Take decimal input from user
decimal_number = float(input("Enter a decimal number: "))

# Output the decimal number
print(f"You entered: {decimal_number}")
print(f"Integer part: {int(decimal_number)}")
print(f"Fractional part: {decimal_number - int(decimal_number):.2f}")
