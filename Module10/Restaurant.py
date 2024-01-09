
class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name = name 
        self.orders =[]
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0
        
        
    def add_employee(self,employee_type,emplyee):
        if employee_type =='chef':
            self.chef = emplyee
            
        elif employee_type=='server':
            self.server=emplyee
            
        elif employee_type=='manager':
            self.manager= emplyee
         
    def add_order(self,order):
        self.orders.append(order)
        
    def receive_payment(self,order,amount,customer):
        print(amount,order.bill)
        if order.bill<=amount: 
            self.revenue +=order.bill
            self.balance +=order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough money .Pay more')
        
    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense+=amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
            
        else:
            print(f'Not enough money to pay {amount}')
            
    def pay_salary(self,employee):
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            print(f"Expense {employee.salary} for {employee.name}'s salary")
            employee.receive_salary(self)
            
    def show_employee(self):
        print(f'-----------SHOWING EMPLOYEE-----------')
        if self.chef is not None:
          print(f'Chef: {self.chef.name} with salary: {self.chef.salary}')
        if self.server is not None:
          print(f'Chef: {self.server.name} with salary: {self.server.salary}')
        if self.manager is not None:
          print(f'Chef: {self.manager.name} with salary: {self.manager.salary}')
          

        
        
    