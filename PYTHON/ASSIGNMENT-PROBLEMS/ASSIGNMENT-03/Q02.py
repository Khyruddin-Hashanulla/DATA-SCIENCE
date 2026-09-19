"""
Q2. Given a list of integers compute the average of all numbers in the list.
"""

list = [7, 4, 3, 4, 5, 6]
sum = 0

for li in list:
    sum+=li
print(f"Average of list is: {(sum/len(list)):.2f}")
