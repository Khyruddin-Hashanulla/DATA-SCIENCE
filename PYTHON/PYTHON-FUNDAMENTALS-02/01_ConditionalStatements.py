# Conditional Statements in Python
# Example of if-else statement
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example of if-elif-else statement
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Example of nested if statements
number = 10
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

# Example of using logical AND operators in conditional statements
age = 25
income = 50000
if age >= 18 and income >= 40000:
    print("You are eligible for a loan.")

# Example of using logical OR operators in conditional statements
age = 16
if age < 18 or age > 65:
    print("You are not eligible for this program.")

# Example of using logical NOT operator in conditional statements
is_student = False
if not is_student:
    print("You are not a student.")

# Example of using the ternary operator (conditional expression)
score = 75
result = "Pass" if score >= 50 else "Fail"
print("Result: ", result)

# Example of Login System using if-else statements
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
elif username == "admin":
    print("Incorrect password.")
else:
    print("Username not found.")

# WAP to check if N is a multiple of 5 or not
n = 10
if n % 5 == 0:
    print("N is a multiple of 5.")
else:
    print("N is not a multiple of 5.")
