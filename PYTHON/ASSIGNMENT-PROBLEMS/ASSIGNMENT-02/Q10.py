"""
Q10. Let's create a "Number Guessing Game". Given a secret number (Already decided by you, Write a program that asks the user to guess it and prints:
- Too High, If the guess is above the number
- Too Low, If the guess is below
- Correct!, If the guess is correct
"""

n = 75

while True:
    guess = int(input("Guess the number: "))

    if guess > n:
        print("Too High")
    elif guess < n:
        print("Too Low")
    else:
        print("Correct!")
        break
