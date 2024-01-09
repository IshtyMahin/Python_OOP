
class Calculator:
    brand= 'Casio MS990'
    
    def add(self,num1,num2):
        return num1+num2
    
    def deduct(self,num1,num2):
        return num1-num2
    
    def multiply(self,num1,num2):
        return num1*num2
    
    def divide(self,num1,num2):
        return num1/num2
    

cal = Calculator()

print(cal.add(3,4))
print(cal.deduct(3,4))
print(cal.multiply(3,4))
print(cal.divide(3,4))

