n = int(input())

ls = list(map(int,input().split(" ")))

mn = max(ls)
for i in ls:
    c=0
    while i%2==0:
        i/=2
        c+=1
    
    mn = min(c,mn)
    
print(mn)
        