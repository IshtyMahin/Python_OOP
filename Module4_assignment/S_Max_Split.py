s = input()
r=0
l=0
lt = list()
for i in range(len(s)):
    if s[i]=='R':
        r+=1
    else :
        l+=1
    
    if( r==l):
        # print(i,r,l)
        lt.append(s[i-r-l+1:i+1])
        r=0
        l=0
    
print(len(lt))
print('\n'.join(lt))
        