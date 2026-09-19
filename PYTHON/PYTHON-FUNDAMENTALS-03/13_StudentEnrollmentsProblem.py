"""
STUDENT ENROLLMENTS -
Given a list of tuples with info (name, subject):
- List all unique course
- List students enrolled in english
- Create dictionary (student, set of courses)
"""

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# - List all unique course
unique_courses_set = set()

for tup in info:
    unique_courses_set.add(tup[1])
print(unique_courses_set)

# - List students enrolled in english
for name,course in info:
    if course == "English":
        print(name)

# - Create dictionary (student, set of courses)
dict = {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
