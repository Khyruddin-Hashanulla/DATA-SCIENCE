# With Keyword in Python is used to simplify the management of resources, such as file handling.
# It ensures that resources are properly acquired and released, even if an error occurs during their usage.
# The most common use of the with keyword is in file handling, where it automatically takes care of closing the file after its block of code is executed.

with open("PYTHON/PYTHON-FUNDAMENTALS-05/Sample.txt", "r") as f:
    content = f.read()
    print(content)
