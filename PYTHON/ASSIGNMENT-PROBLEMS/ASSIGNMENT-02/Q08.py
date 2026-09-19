"""
Q8. WAF create a Simple Calculator that performs arithmetic operations. Create
a function calculator(a, b, operation) that performs addition, subtraction,
multiplication, or division based on the operation parameter.

[Operation Parameter can have values '+', '-', '*' & '/']
"""

def calculator(a, b, operation):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b

# Function Calls
print(calculator(5, 2, "+"))
print(calculator(5, 2, "-"))
print(calculator(5, 2, "*"))
print(calculator(5, 2, "/"))
