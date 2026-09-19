# JSON Module
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data between a server and a web application as text.

import json

# Example 1: Converting a Python object to a JSON string
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}

# Convert Python object to JSON string
json_string = json.dumps(data, indent=4)  # indent for pretty printing
print("JSON String:")
print(json_string)

# Example 2: Converting a JSON string back to a Python object
json_data = '{"name": "Jane Doe", "age": 25, "city": "Los Angeles", "is_student": true, "courses": ["English", "Art"]}'
python_object = json.loads(json_data)
print("Python Object:")
print(python_object)

# Example 3: Writing JSON data to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Example 4: Reading JSON data from a file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Loaded Data from File:")
    print(loaded_data)
