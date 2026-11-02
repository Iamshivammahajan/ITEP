'''
Bank Account Simulation
Problem

Design a banking system using OOP.

Requirements

Each account should contain:

account number
holder name
balance
Functionalities
Deposit money
Withdraw money
Prevent withdrawal if balance insufficient
Display account summary
Maintain bank-wide interest rate as class variable
Add static method to validate minimum balance rule
Concepts Practiced
object state management
static methods
class variables
validations
'''

class BankAccount:
    def __init__(self):
        self.__acc_no = None
        self.__name = None
        self.__bal = 0.00

    def set_accno(self, num):
        self.__acc_no = num

    def set_name(self, name):
        self.__name = name

    def set_balance(self, bal):
        self.__bal = bal

    def display(self):
        print(f"Account No. : {self.__acc_no} Account Holder : {self.__name} Balance : {self.__bal}")

obj = BankAccount()
num = input("Enter Account Number : ")
name = input("Enter Name : ")
bal = float(input("Enter Balance : "))

obj.set_accno(num)
obj.set_name(name)
obj.set_balance(bal)
obj.display()

