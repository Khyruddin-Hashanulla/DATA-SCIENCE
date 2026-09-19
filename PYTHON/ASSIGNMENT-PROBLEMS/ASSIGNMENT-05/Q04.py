"""
Q4. Create a Python dictionary of 3 cities and their populations. Save it to "cities.json":
    1. Then load the JSON and print each city and its population.
    2. Ask the user for a new city & its population - update this info in the json file
"""

import json

# 1. Create a dictionary of 3 cities and their populations
cities = {
    "Kolkata": 15_000_000,
    "Delhi": 33_000_000,
    "Mumbai": 21_000_000
}

# Save dictionary to cities.json
with open("PYTHON/ASSIGNMENT-PROBLEMS/ASSIGNMENT-05/cities.json", "w") as file:
    json.dump(cities, file, indent=4)


# 2. Load the JSON file
with open("PYTHON/ASSIGNMENT-PROBLEMS/ASSIGNMENT-05/cities.json", "r") as file:
    cities = json.load(file)

# Print each city and its population
for city, population in cities.items():
    print(f"{city}: {population}")


# 3. Ask user for a new city and population
new_city = input("Enter a new city: ")
new_population = int(input("Enter its population: "))

# Update the dictionary
cities[new_city] = new_population

# Save the updated dictionary back to JSON
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

print("City added successfully!")
