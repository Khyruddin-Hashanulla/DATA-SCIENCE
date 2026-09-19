"""
Q1. Ask the user for a string and check whether it is a palindrome or not.
- A Palindrome is a string which is same wehn we read it forward and backward. Eg. madam, racecar
"""

string = input("Enter a Word to check is it Palindrome or Not: ").lower()
reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print(True)
else:
    print(False)
