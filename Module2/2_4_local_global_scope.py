# you can access global variable without using the global keyword

# if you want to modify a global variable, you have to use the global keyword

balance =1000

def buy_thing(item,price):
    dream_phone = 'xphone'
    # balance = balance-price;
    global balance
    print(f"previous balance value",balance)
    balance=balance-price
    print(f"balance after buying {item}",balance)
    
# print(dream_phone)
buy_thing("sunglass",600)
print('global balance after buy',balance)