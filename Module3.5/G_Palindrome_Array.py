# n = int(input())
# l= (input())

# l = list(l.split(" "))
# p = l[::-1]
# # print(l)
# ans=1
# for i in range(n):
#     if l[i]!=p[i]:
#         ans=0
#         break
    
# if ans==1:
#     print("YES")
# else:
#     print("NO")
    
n = int(input())
l = input().split()

if l == l[::-1]:
    print("YES")
else:
    print("NO")
