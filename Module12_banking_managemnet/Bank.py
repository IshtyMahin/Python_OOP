class Bank:
    def __init__(self, name, initial_balance) -> None:
        self.name = name
        self.balance = initial_balance
        self.loan_feature = True
        self.users = []
        self.admins = []
        
        