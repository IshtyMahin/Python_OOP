
class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print('Vat mangso polau korma')
        
    def exercise(self):
        raise NotImplementedError
    
    
        

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team =team
        super().__init__(name, age, height, weight)
    
    #override
    def eat(self):
        print('vegetables')
    
    #overload
    def exercise(self):
        print('gym e poisa diya hudai ghma jorai')
        
    # + sign operator overladd
    def __add__(self,other):
        return self.age+other.age
    
    # * sign overload
    def __mul__(self,other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    # > sign overload
    def __gt__(self,other):
        return self.age>other.age        
sakib = Cricketer('Sakib',38,68,91,'BD')
mushi = Cricketer('mushi',36,65,78,'BD')
sakib.eat()
sakib.exercise()

# plus sign overload
print(45+64)
print('sakib'+"rakib")
print([12,34,64]+[123,45])
print(sakib+mushi)
print(sakib*mushi)
print(sakib>mushi)