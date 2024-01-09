# encapsulation --> hide details
# access modifier: public, protected,priate
class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name # public
        self._branch= 'fatickchari' # underscore(_) protected
        self.__balance = initial_deposit # double underscore(__) private
        
    def deposit(self,amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
        
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return f"New balance {self.__balance}"
        else:
            return f"Fokir , taka nai"
        
ishty = Bank('Ishtiaq',10000)
print(ishty.holder_name)
# ishty.balance=0

print(ishty.get_balance())
print(ishty.withdraw(2345))
# print(dir(ishty))
# print(ishty._Bank__balance)