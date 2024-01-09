
from datetime import datetime

class User:
    # initaially_balance =0, account number will be generate auto matically
    def __init__(self, name, email, address, account_type, bank):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.bank = bank
        self.account_number = None
        self.balance = 0.0
        self.transaction_history = []
        self.loan = 0
        self.loan_amount=0
    
    # create an account of user 
    def create_an_account(self):
        self.bank.users.append(self)
        self.account_number = len(self.bank.users)  
        return self

    #deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.bank.balance += amount
            print(f'You deposited {amount} tk successfully. New Balance: {self.balance}')
            self.transaction_history.append(f'Deposit: {amount}, Current Balance: {self.balance}, Time: {datetime.now()}')
        else:
            print("Failed Deposit.")

    # If the withdrawal amount is more than the current balance, show an error message that “Withdrawal amount exceeded” 	
    def withdraw(self, amount):
        
        if amount > self.balance:
            print(f"You don't have enough deposit money to withdraw {amount} tk")
        elif amount <= 0:
            print("Failed. Give a positive amount")
        if amount > self.bank.balance:
            print('Sorry, the Bank is bankrupt')
        else:
            self.balance -= amount
            self.bank.balance -= amount
            print(f'You withdrew {amount} tk successfully. New Balance: {self.balance}')
            self.transaction_history.append(f'Withdraw: {amount}, Current Balance: {self.balance}, Time: {datetime.now()}')

    # check balannce
    def check_balance(self):
        return self.balance

    # check transaction history
    def check_transaction_history(self):
        print("---Your transaction history---")
        for his in self.transaction_history:
            print(his)

    # take loan
    def take_loan(self, amount):
        # atmost two times
        if self.loan < 2:
            self.balance += amount
            self.bank.balance += amount
            self.loan += 1
            self.loan_amount += amount
            print(f'Loan of {amount} tk added to your account. New Balance: {self.balance}')
            self.transaction_history.append(f'Loan: {amount}, Current Balance: {self.balance}, Time: {datetime.now()}')
        else:
            print("Sorry, you have already taken 2 loans")

    # transfer amount to another account in same bank
    # if the other account doesnot exist then show an error message "Account does not exist" 
    def transfer_amount(self, other, amount):
        if other not in self.bank.users:
            print("The account does not exist in the bank")
        elif amount > self.bank.balance:
            print('Sorry, the Bank is bankrupt')
        elif amount > self.balance:
            print(f"You don't have enough deposit money for the transfer of {amount} tk")
        elif amount <= 0:
            print("Failed. Give a positive amount")
        elif other == self:
            print("Both are the same account")
        else:
            self.balance -= amount
            other.balance += amount
            # self account
            print(f'{self.name} transferred {amount} tk to {other.name} successfully. New Balance: {self.balance}')
            self.transaction_history.append(f'Transfer: {amount}, Current Balance: {self.balance}, Time: {datetime.now()}')
            
            # other account
            print(f'{other.name} received {amount} tk from {self.name} successfully. New Balance: {other.balance}')
            other.transaction_history.append(f'Receive: {amount}, Current Balance: {other.balance}, Time: {datetime.now()}')
            

    # User can only withdraw and transfer money from his account if he has money in his account
    
    # if a user is unable to withdreaw the amount of money he has deposited in the bank ,he will get a message that the bank is bankrupt