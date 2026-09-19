"""
Q3. Input two lists of integers from the user. Merge them into one list and sort the
result.
"""

list1 = []
list2 = []

input1 = input("Enter List 1: ").split()
input2 = input("Enter List 2: ").split()

for value in input1:
    list1.append(int(value))

for value in input2:
    list2.append(int(value))

merge_list = list1 + list2
merge_list.sort()

print(f"Sorted list: {merge_list}")
