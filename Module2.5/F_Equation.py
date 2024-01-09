p= (input())
x,y = (p.split(" "))
x= int(x)
n = int(y)

s=0
def power(p,q):
    pw = 1
    for i in range(1,q+1):
        pw*=p
     
    return pw
        
for i in range(2,n+1,2):
    s= s+ power(x,i)

print(s)
