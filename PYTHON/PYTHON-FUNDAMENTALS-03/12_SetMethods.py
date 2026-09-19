# Set Methods in Python

sets = {1, 6, 2, 2, 8, 11}
sets2 = {1, 6, 2, 15, 51}

# Add - Add a Value
sets.add(19)
print(sets)

# Remove - Remove a Value
sets.remove(8)
print(sets)

# Clear - Empty a Set
# sets.clear()
# print(sets)

# Pop - Remove Random Value
sets.pop()
print(sets)

# Union - Return new union
print(sets.union(sets2))

# Intersection - Return new Intersection
print(sets.intersection(sets2))
