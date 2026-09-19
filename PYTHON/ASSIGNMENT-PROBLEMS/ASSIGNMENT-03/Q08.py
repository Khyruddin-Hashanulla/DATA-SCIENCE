"""
Q8. Write a program to check weather two lists share no common elements.
"""

list1 = [1, 2, 3, 4]
list2 = [1, 6, 7, 8]

common = False

for item in list1:
    if item in list2:
        common = True
        break

if common:
    print("Lists have common elements")
else:
    print("Lists have no common elements")
