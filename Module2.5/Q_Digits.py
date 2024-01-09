t = int(input())

while(t):
    x = input()

    x=x[::-1]
    
    for i in x:
        print(i,end=" ")
    print()
    t-=1
    
