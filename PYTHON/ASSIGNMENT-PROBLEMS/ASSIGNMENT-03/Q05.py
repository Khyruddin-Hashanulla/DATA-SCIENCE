"""
Q5. Create a dictionary where:
- Key = Students Name
- Values = Marks (Integer)

Write a Menu-Based Program where user passes a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the dictionary:
1. A - Add a Student
2. B - Update Marks
3. C - Search for a Student
4. D - Display all Students and Marks
"""

info = {
    "Khyruddin" : 85,
    "Harsh" : 75,
}

while True:
    print("\n--- Student Marks Menu ---")
    print("A - Add a Student")
    print("B - Update Marks")
    print("C - Search for a Student")
    print("D - Display all Students and Marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        info[name] = marks
        print("Student added successfully!")

    elif choice == "B":
        name = input("Enter student name: ")

        if name in info:
            marks = int(input("Enter new marks: "))
            info[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    elif choice == "C":
        name = input("Enter student name: ")

        if name in info:
            print(f"{name}'s marks: {info[name]}")
        else:
            print("Student not found.")

    elif choice == "D":
        print("\n--- All Students ---")

        for name, marks in info.items():
            print(f"{name}: {marks}")

    elif choice == "E":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
