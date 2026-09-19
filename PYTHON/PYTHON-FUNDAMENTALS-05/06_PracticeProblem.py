# We will search a particular word in a file.

data = True
line = 1
with open("PYTHON/PYTHON-FUNDAMENTALS-05/Sample.txt", "r") as f:
    while data:
        data = f.readline()
        if "Data Science" in data:
            print(f"Line {line}: {data}")
            break
        line += 1
