# Break & Continue Statements in Python
# Example of using break statement in a loop

count = 0
while count < 10:
    if count == 5:
        break  # Exit the loop when count is 5
    print("Count:", count)
    count += 1

# Example of using continue statement in a loop
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print("Odd Count:", count)
