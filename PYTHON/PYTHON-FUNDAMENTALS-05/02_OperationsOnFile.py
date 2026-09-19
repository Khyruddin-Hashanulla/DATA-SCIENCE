# Operations on Files in Python
# In Python, you can perform various operations on files, such as reading, writing, appending, and deleting files.
# Here are some common file operations:

f = open("PYTHON/PYTHON-FUNDAMENTALS-05/Sample.txt", "w")

# content = f.read()
# content = f.readline()
# content = f.readlines()
# content = f.readable()
content = f.write("""What is Data Science?
->Data science is the study of data used to extract meaningful insights for business decisions.
It combines mathematics, computing and domain knowledge to solve real-world problems and uncover
hidden patterns.

It processes raw data to address business challenges and predict future trends.
For example, from large company datasets, data science can help answer questions like:
- What do customer want?
- How can we improve our services?
- What will the upcoming trend in sales?
- How much stock they need for upcoming festival.""")

print(content)

f.close()
