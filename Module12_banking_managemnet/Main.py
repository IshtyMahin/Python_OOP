
from Bank import Bank
from Admin import Admin
from User import User

def main():
    myBank = Bank("MyBank", 1000000)
    admin = Admin("admin", "admin_pass", myBank)
    Ishtiaq = User("ishtiaq uddin", "ishtiaq@uddin.com", "Fatikchari", "Savings",myBank).create_an_account()
    Mahin = User("Mahin Chowdhury", "Mahin@chy.com", "Chittagong", "Savings",myBank).create_an_account()
    Maruf = User("Maruf Chowdhury", "Maruf@chy.com", "Fatikchari", "Savings",myBank).create_an_account()


    def user_info(select_user):
        while True:
                print("\n----Options-----")
                print("1. View Balance")
                print("2. Deposit Balance")
                print("3. Withdraw Balance")
                print("4. View Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Exit")
                print("----  o -----\n")

                user_opt = int(input("Enter your option: "))

                if user_opt == 1:
                    print(f"Balance: {select_user.check_balance()}")
                elif user_opt == 2:
                    amount = float(input("Enter deposit amount: "))
                    select_user.deposit(amount)
                elif user_opt == 3:
                    amount = float(input("Enter withdraw amount: "))
                    select_user.withdraw(amount)
                elif user_opt == 4:
                    select_user.check_transaction_history()
                elif user_opt == 5:
                    amount = float(input("Enter loan amount: "))
                    select_user.take_loan(amount)
                elif user_opt == 6:
                    other_account_number = int(input("Enter other's account number: "))
                    other_account = None
                    for user in myBank.users:
                        if user.account_number == other_account_number:
                            other_account = user
                            break
                    if other_account:
                        amount = float(input("Enter transfer amount: "))
                        select_user.transfer_amount(other_account, amount)
                    else:
                        print("Other account not found.")
                elif user_opt == 7:
                    break
                else:
                    print("Invalid option. Please try again.")


    while True:
        print("\n----Options-----")
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        print("----  o -----\n")

        opt = int(input("Enter your Option: "))

        if opt == 1:
                while True:
                    print("\n----Options-----")
                    for index,user in enumerate(myBank.users,start=1):
                        print(f"{index}. {user.name}")
                    
                    print(f"{len(myBank.users)+1}. Exit")
                    
                    opt = int(input(f"Enter your Option (1 to {len(myBank.users)+1}): "))
                    if opt == len(myBank.users)+1:
                        break
                    user = myBank.users[opt - 1]
                    user_info(user)
                    
                
        elif opt == 2:
            while True:
                
                
                print("\n----Options-----")
                print("1. Delete User Account")
                print("2. View All Users")
                print("3. View total bank balance")
                print("4. View total bank loan")
                print("5. Change Loan Feature")
                print("6. Exit")
                print("\n-------  o ------")
                admin_opt = int(input("Enter your Option: "))

                if admin_opt == 1:
                    account_number = int(input("Enter account number to delete: "))
                    account = None
                    for user in myBank.users:
                        if user.account_number == account_number:
                            account = user
                            break
                        
                    if account:
                        admin.delete_user(account)
                    else:
                        print("User not found.")
                elif admin_opt == 2:
                    admin.view_user_accounts()
                elif admin_opt == 3:
                    print(f"Total Bank Balance: {admin.total_balance()}")
                elif admin_opt == 4:
                    print(f"Total Loans: {admin.total_loans()}")
                    print(f"Total Loans_amount: {admin.total_loans_amount()}")
                elif admin_opt == 5:
                    admin.toggle_loan_feature()
                elif admin_opt == 6:
                    break
                else:
                    print("Invalid option. Please try again.")

        elif opt == 3:
            break
        else:
            print("Invalid option. Please try again.")
        

if __name__ == "__main__":
    main()