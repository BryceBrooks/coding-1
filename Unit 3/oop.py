# Create a new python file called oop.py review the following 
# w3school articles and answer the following questions

# 1. In a few sentences describe the difference between a class constructor 
# and an object

# 2. In a few sentences describe the difference between an object property 
# and an object method

# 3. You have been tasked with creating a digital book inventory system. Create 
# a class called book. Your class should have 3 properties and 2 methods

# 4. You have been tasked with creating a bank system. Create a class for a user 
# account for the bank system. Your class should include 3 properties and 2 methods


# oop.py

# Question 3: Digital Book Inventory System

class Book:
    # Constructor with 3 properties
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    # Method 1: Display book information
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Copies: {self.copies_available}")

    # Method 2: Borrow a book
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"You borrowed '{self.title}'.")
        else:
            print("Sorry, no copies are available.")


# Question 4: Bank Account System

class BankAccount:
    # Constructor with 3 properties
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    # Method 1: Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Method 2: Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Insufficient funds.")


# Testing the Book class
print("=== Book Inventory System ===")

book1 = Book("Harry Potter", "J.K. Rowling", 5)

book1.display_info()
book1.borrow_book()
book1.display_info()


# Testing the BankAccount class
print("\n=== Bank Account System ===")

account1 = BankAccount("John Smith", "123456", 500.00)

account1.deposit(200)
account1.withdraw(100)

print(f"Account Holder: {account1.account_holder}")
print(f"Account Number: {account1.account_number}")
print(f"Current Balance: ${account1.balance:.2f}")
