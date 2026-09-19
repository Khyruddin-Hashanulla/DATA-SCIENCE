"""
Q7. Design a program to continuously input a number N from user & print if it is
positive or negative until the user enters “Quit”.
"""

while True:
    user_input = input("Enter Number or Quit: ")
    if user_input == "QUIT" or user_input == "quit":
        break
    n = int(user_input)
    if n < 0:
        print("Negative Number")
    elif n > 0:
        print("Positive Number")
    else:
        print("Zero")
