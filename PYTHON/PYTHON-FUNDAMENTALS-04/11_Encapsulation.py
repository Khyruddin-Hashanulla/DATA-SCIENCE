# Encapsulation in Python is a fundamental concept in object-oriented programming that restricts access to certain attributes and methods of a class. It helps to protect the internal state of an object and ensures that it can only be modified through well-defined interfaces.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    # Public method to check balance
    def get_balance(self): # Getter method to access the private attribute __balance
        return self.__balance

# Creating an instance of BankAccount
account = BankAccount("123456789", 1000)

# Accessing public methods
account.deposit(500)  # Deposited: 500. New Balance: 1500
account.withdraw(200)  # Withdrew: 200. New Balance: 1300
print(f"Current Balance: {account.get_balance()}")  # Current Balance: 1300
