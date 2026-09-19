"""
Q6. Create an abstract class Employee with an abstract method calculate_salary().
Create sub-classes Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Example usage
intern = Intern(1000)
full_time_employee = FullTimeEmployee(50000, 5000)
contract_employee = ContractEmployee(50, 160)
print(f"Intern Salary: {intern.calculate_salary()}")
print(f"Full-Time Employee Salary: {full_time_employee.calculate_salary()}")
print(f"Contract Employee Salary: {contract_employee.calculate_salary()}")
