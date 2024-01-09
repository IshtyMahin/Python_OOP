
class Product:
    def __init__(self,product_name) -> None:
        self.product_name = product_name
        

class Shop:

    def __init__(self,name) -> None:
        self.name = name
        self.productList=[]
    def add_product(self,product_name):
        product = Product(product_name)
        self.productList.append(product)
        
    # def buy_product(self,item):
        
    #     for product in self.productList:
    #         if product.product_name == item:
    #             print(f"You buy a product: {item}")
    #             return
            
    #     print(f"{item} is not available in the shop ")
    
    def buy_product(self, item):
        try:
            product = next(product for product in self.productList if product.product_name == item)
            # self.productList.remove(product)
            print(f"You bought a product: {item}")
        except StopIteration:
            print(f"{item} is not available in the shop")


AmarShop = Shop("AmarShop")

AmarShop.add_product("Alu")
AmarShop.add_product("Rice")

AmarShop.buy_product("Dim")
AmarShop.buy_product("Alu")