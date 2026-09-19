"""
Q7. Ask the user for a temperature in Celsius (string input). Convert it to float and,
then calculate and print temperature in Fahrenheit.

Formula: F = (C * 9/5) + 32
"""

celsius = input("Enter temperature in Celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit}")
