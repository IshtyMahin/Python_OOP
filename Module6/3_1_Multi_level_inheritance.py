class Vehicle:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
        
    def move(self):
        pass
    
    def __repr__(self) -> str:
        return f'{self.name}  {self.price}'
    
class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat= seat
        super().__init__(name, price)
        
    def __repr__(self) -> str:
        
        return f'{super().__repr__()} {self.seat}'
        
class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight= weight
        super().__init__(name, price)
        
class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        
class ACBus(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperatur= temperature
        super().__init__(name, price, seat)
        
    def __repr__(self) -> str:
        return f'{super().__repr__()} {self.temperatur}'
        
green_line = ACBus('green',5000000,22,16)

print(green_line)