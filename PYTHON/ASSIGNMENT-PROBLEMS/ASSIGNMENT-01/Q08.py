"""
Q8. Take the radius (r) as a user input and calculate the area of a circle using the formula: Area = π * r^2. Use 3.14 for π. Print the area rounded to 2 decimal places.
"""

radius = input("Enter the radius of the circle: ")
area = 3.14 * (float(radius) ** 2)
print(f"Area of the circle: {area:.2f}")
