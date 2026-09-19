"""
WAF that prints the digits of a given number. For example, if the input number is 1234, the output should be:
1
2
3
4

Hint: The right most digit can be obtained by taking the modulus of the number with 10. The leftmost digit can be obtained by dividing the number by 10.
"""

def print_digits(number):
    if number < 0:
        print("Invalid input")
        return

    place = 1
    while number // place >= 10:
        place *= 10

    while place > 0:
        digit = number // place
        print(digit)
        number %= place
        place //= 10

# Function call
print_digits(1234)
