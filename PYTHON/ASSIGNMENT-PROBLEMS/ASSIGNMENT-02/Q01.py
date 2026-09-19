"""
Q1. Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on the following rules:
• If salary < 30,000 → 5%
• If salary is 30,000–70,000 → 15%
• If salary > 70,000 → 25%
"""

salary = float(input("Enter your salary: "))
if salary < 30000:
    tax_rate = 0.05
elif 30000 <= salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

print(f"Your tax rate is: {salary * tax_rate:.2f} ({tax_rate * 100}%)")
