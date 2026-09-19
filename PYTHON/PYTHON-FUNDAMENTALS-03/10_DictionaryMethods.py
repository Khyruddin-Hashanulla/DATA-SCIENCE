# Dictionary Methods in Python

info = {
    "name" : "Khyruddin",
    "age" : 23,
    "cgpa" : 7.5,
    "degree" : "B.Tech, CSE",
    3.14 : "PI",
    "subjects" :["Physics", "Chemestry", "Math", "Biology"]
}

# Keys - To returns all keys
print(info.keys())

# Values - To returns all values
print(info.values())

# Items - To returns all key:values pairs
print(info.items())

# Get - To return value acc. to key
print(info.get("name"))

# Update - Adds new item to dist
info.update({
    "stream" : "Computer Science And Engineering"
})

print(info.items())
