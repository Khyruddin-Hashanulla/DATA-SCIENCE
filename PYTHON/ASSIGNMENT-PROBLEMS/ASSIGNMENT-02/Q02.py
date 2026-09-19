"""
WAF that takes two integers a and b and prints all even numbers between a and b (inclusive). If a is greater than b, print "Invalid input".
"""
def print_even_numbers(a, b):
    if a > b:
        print("Invalid input")
    else:
        for i in range(a, b + 1):
            if i % 2 == 0:
                print(i)

# Function call
print_even_numbers(2, 10)
