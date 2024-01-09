""" 
1. calculator class to do add, deduct, multiply, divide
2. Pen class. create three object with different instance attribute
3. Exam attend_to_exam get_marks 
 """
 
class Pen:
     def __init__(self,company_name,price) -> None:
         self.company_name = company_name
         self.price=price
    
     def __repr__(self) -> str:
          return f"Company_name :{self.company_name} , Price :{self.price}"
         

Matador = Pen("Matador",10)
print(Matador)
GoodLuck = Pen("GoodLuck",5)
print(GoodLuck)
i_teen = Pen("i_teen",6)
print(i_teen)

          