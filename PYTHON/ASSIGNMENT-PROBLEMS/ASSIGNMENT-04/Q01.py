"""
Q1. Create a BankAccount class with attributes account_number, account_holder, and balance.
Implement methods to deposit, withdraw, and check the balance of the account.
"""

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance for {self.account_holder}: {self.balance}")

Account = BankAccount("123456789", "John Doe", 1000)
Account.check_balance()
Account.deposit(500)
Account.withdraw(200)
Account.check_balance()
