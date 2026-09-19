"""
Q4. WAF to return the count of the number of digits in a given number.
"""

def count_digits(number):
    count_digits = 0
    while number > 0:
        number //= 10
        count_digits += 1
    return count_digits

print(count_digits(12342463))
