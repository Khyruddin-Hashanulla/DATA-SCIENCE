"""
Q7. Write a program that takes a string from the user and prints the number of spaces in the string
"""

text = input("Enter a string: ")
space = 0

for char in text:
    if char == " ":
        space += 1

print("Number of spaces:", space)
