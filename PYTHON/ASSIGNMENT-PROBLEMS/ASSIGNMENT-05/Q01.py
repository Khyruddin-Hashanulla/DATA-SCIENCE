"""
Q1. Create a Program that:
    1. Opens a file "names.txt" in write mode.
    2. Writes 5 names(One per line) entered by the user
    3. Then opens the same file in read mode and prints all names
"""

with open("PYTHON/ASSIGNMENT-PROBLEMS/ASSIGNMENT-05/names.txt", "w") as f:
    for i in range(5):
        name = input(f"Enter name {i + 1}: ")
        f.write(name + "\n")

with open("PYTHON/ASSIGNMENT-PROBLEMS/ASSIGNMENT-05/names.txt", "r") as f:
    print("\nNames in the file:")
    print(f.read())
