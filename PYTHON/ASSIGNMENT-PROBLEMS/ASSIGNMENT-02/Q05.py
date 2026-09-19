# WAF to return the sum of digits of a given number

def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum
print(sum_of_digits(123))
