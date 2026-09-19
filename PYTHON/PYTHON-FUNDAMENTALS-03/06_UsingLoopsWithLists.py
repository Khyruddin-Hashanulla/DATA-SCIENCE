# Using Loops With Lists in Python

nums = [1, 3, 5, 7, 9]
x = 7
idx = 0

for val in nums:
    if val == x:
        print(f"{x} is at {idx} index")
        break
    idx += 1
