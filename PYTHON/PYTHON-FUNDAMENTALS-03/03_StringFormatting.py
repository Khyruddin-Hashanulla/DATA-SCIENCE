# String Formatting in Python - f-string and format()

a = 10
b = 2
sum = a + b

# Normal Formatting
print("Sum of {} + {}: {}".format(10,2,sum))

# Index based Formatting
print("Sum of {1} + {0}: {2}".format(10,2,sum))

# Value Based Formatting
print("Values of vars {c} & {d}".format(c = 3, d = 20))

# f-strings
print(f"Multiplication of {a} and {b}: {a*b}")
