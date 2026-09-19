"""
Q10. Ask the user for a string and print:
    - All unique characters
    - The count of unique characters
"""

words = input("Enter a string: ")
unique = set()

for char in words:
    if words.count(char) == 1:
        unique.add(char)

print("Unique characters:", unique)
print("Count of unique characters:", len(unique))
