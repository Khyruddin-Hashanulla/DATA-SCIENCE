"""
Q9. Given a list, print all elements that appear more than once in the list.
"""

list1 = [7, 4, 3, 4, 5, 6, 1, 3]
duplicate = set()

for item in list1:
    if list1.count(item) > 1:
        duplicate.add(item)

print(duplicate)
