"""
Q2. Create a Program that:
    1. Opens a file "log.txt" in append mode.
    2. Adds a new log entry (like "Program run successfully")
    3. Then opens the same file in read mode and prints all names
"""

# 1. Open log.txt in append mode
with open("PYTHON/ASSIGNMENT-PROBLEMS/ASSIGNMENT-05/log.txt", "a") as file:
    file.write("Program run successfully\n")

# 2. Open the same file in read mode
with open("PYTHON/ASSIGNMENT-PROBLEMS/ASSIGNMENT-05/log.txt", "r") as file:
    content = file.read()

# 3. Print all log entries
print(content)
