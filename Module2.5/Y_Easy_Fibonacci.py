n = int(input())

if n==1:
    print(0)
else:
    print(0,1,end=" ")
x=0
y=1
for i in range(n-2):
    print(x+y,end=" ")
    tmp = x
    x=y
    y=tmp+y
