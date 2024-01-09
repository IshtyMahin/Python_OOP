
class Shopping:
    cart = [] # class attribute # static attribute
    origin = 'china'
    
    def __init__(self,name,location) -> None:
        self.name = 'Jamu na city' # instance attribute
        self.location = 'Jam er maj khane'
        
    def purchase(self,item,price,amount):
        remaining = amount-price
        
        print(f'buying: {item} for price: {price} and remaining: {remaining}')
        

Shopping.purchase('a',2,3,3)