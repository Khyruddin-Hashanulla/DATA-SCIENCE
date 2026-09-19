"""
Q9. Ask the user for: Principal amount (P), Rate of interest (R), and Time (T) in years. Calculate the Simple Interest using the formula: SI = (P * R * T) / 100. Convert all to float and print the Simple Interest rounded to 2 decimal places.
"""

principal = input("Enter the principal amount (P): ")
rate = input("Enter the rate of interest (R): ")
time = input("Enter the time in years (T): ")
simple_interest = (float(principal) * float(rate) * float(time)) / 100
print(f"Simple Interest: {simple_interest:.2f}")
