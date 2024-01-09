n = int(input())
ls = list(map(int,input().split(" ")))

freq ={}

for i in ls:
    if i in freq:
        freq[i]+=1
    else :
        freq[i]=1
        
c=0
for key,val in freq.items():
    if key != val:
        if key>val:
            c+=val
        else:
            c+= (val-key)

print(c)