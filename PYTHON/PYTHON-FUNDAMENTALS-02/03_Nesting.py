# Nesting Conditional Statements
username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == "admin" and password == "password123"):
    print("Login successful!")
else:
    if username != "admin":
        print("Username not found.")
    else:
        print("Incorrect password.")
