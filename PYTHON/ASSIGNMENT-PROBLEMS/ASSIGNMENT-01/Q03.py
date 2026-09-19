"""
Q3. Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
"""

num1 = int(input("Please Enter The First Integer: "));
num2 = int(input("Please Enter The Second Integer: "));
num3 = float(input("Please Enter A Float: "));

num1 = float(num1);
num2 = float(num2);
average = (num1 + num2 + num3) / 3;
print(f"The Average of {num1}, {num2} and {num3} is: {average}");
