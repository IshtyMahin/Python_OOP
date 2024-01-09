
from User import User

class Admin:
    def __init__(self, username, password, bank):
        self.username = username
        self.password = password
        self.bank = bank
        self.bank.admins.append(self)

        
    def create_user(self, name, email, address, account_type):
        user = User(name, email, address, account_type, self.bank)
        user.create_an_account()

    def delete_user(self, user):
        if user in self.bank.users:
            self.bank.users.remove(user)
            print(f"{user.name}'s account deleted.")
        else: 
            print("User doesn't exists.")

    def view_user_accounts(self):
        print("--- ALL USER ---")
        for user in self.bank.users:
            print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {user.email}")

    def total_balance(self):
        return self.bank.balance

    def total_loans(self):
        total_loans = 0
        for user in self.bank.users :
          if user.loan:
              total_loans+= user.loan
        return total_loans
    
    def total_loans_amount(self):
        total_loans_amount = 0
        for user in self.bank.users :
          if user.loan:
              total_loans_amount+= user.loan_amount
        return total_loans_amount

    def toggle_loan_feature(self):
        
        if self.bank.loan_feature :
            self.bank.loan_feature =False
            print("Loan feature is OFF")
        else:
            self.bank.loan_feature =True
            print("Loan feature is ON")


