def full_name (first,last):
    name = f'{first} {last}'
    return name

# take parameters in order (serial wise)
# name = full_name('Ishtiaq','uddin')

name = full_name(last='kodu',first='alu')

print(name)

def famous_name(first,last,**addition):
    print(addition)
    #print(addition['title'])
    name = f' {first} {last}'
    
    for key,value in addition.items():
        print(key,value)
    return name
    
name = famous_name(first='Taher',last='Ali',title="Hujur" ,title2="Shayokh")
print(name)

# def function_name(num1,num2,*arg,**kargs):

# return multiple things from an array
def a_lot(num1,num2):
    sum = num1+num2
    mult = num1*num2
    remain = num1-num2
    # return [sum,mult,remain]
    return sum,mult,remain
    

everything= a_lot(55,21)

print(everything)