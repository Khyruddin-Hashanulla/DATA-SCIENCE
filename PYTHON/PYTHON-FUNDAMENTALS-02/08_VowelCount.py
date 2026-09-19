# Vowel Count in a String
word = "Artificial Intelligence"
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"The number of vowels in '{word}' is: {count}")
