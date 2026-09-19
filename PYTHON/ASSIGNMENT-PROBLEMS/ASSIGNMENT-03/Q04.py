"""
Q4. Given a tuple of integers, create:
- A tuple of all even numbers
- A tuple of all odd number
"""

numbers = (2, 7, 11, 13, 16, 19)

odd = ()
even = ()

for n in numbers:
    if n % 2 == 0:
        even += (n,)
    else:
        odd += (n,)

print("Even numbers are:", even)
print("Odd numbers are:", odd)
