# Operator Precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence.
# The precedence order is as follows:
# 1. Parentheses: ()
# 2. Exponentiation: **
# 3. Unary plus and minus: +x, -x
# 4. Multiplication, Division, Floor Division, Modulus: *, /, //
# 5. Addition and Subtraction: +, -
# 6. Comparison Operators: ==, !=, >, <, >=, <=
# 7. Logical NOT: not
# 8. Logical AND: and
# 9. Logical OR: or
# Example:
x = 5
y = 10
result = x + y * 2  # Multiplication has higher precedence than addition
print("Result of x + y * 2: ", result)  # Output: 25
