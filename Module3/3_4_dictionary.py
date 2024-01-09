numbers = [12,56,98,78,56,12,26,98]

person1 = ['Kala chan',"kalipur",23,'student']

# key alue pair
# dictionary
# object 
# hash table
# oerlap with set

person ={'name':'kala pakhi','address':'kaliapur','age':23,'job':'facebooker'}

print(person['job'])
print(person)
print(person.keys())
print(person.values())
person['language']='python'
person['name']='sada pakhi'
del person['age']
print(person)

for key,value in person.items():
    print(key,value)
    
numbers = [12,56,98,78,56,12,6,98]

for i,num in enumerate(numbers):
    print(i,num)