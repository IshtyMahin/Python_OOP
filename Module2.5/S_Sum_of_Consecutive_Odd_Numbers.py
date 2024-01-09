t = int(input())

while(t):
    p= (input())
    x,y = p.split(" ")  
    x= int(x)
    y = int(y)
    s=0
    for i in range(min(x,y)+1,max(x,y)):
        if i%2==1:
            s+=i
    
    print(s)
    t-=1
