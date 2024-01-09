n = int(input())
p = list(map(int,input().split(" ")))

mx = max(p)
mn = min(p)

# print(mx,mn)

for i in range(n):
    if p[i]==mx:
        p[i]=mn     
    elif p[i]==mn:
        p[i]=mx
    

print(*p)


