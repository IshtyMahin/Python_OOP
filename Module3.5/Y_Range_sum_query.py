# n,q = map(int,input().split(" "))


# ar = list(map(int,input().split(" ")))
# # p = list(map(lambda x: int(x),l))
# # print(ar)
# pre = list()

# pre.append(0)
# for i in range(n):
#     pre.append(pre[i]+ar[i])
    
# # print(pre)
# while q:
#     l,r = map(int,input().split(" "))
#     ans = pre[r]-pre[l-1]
#     print(ans)
#     q-=1

n, q = map(int, input().split())
ar = list(map(int, input().split()))

pre = [0] + [sum(ar[:i+1]) for i in range(n)]

while q:
    l, r = map(int, input().split())
    ans = pre[r] - pre[l-1]
    print(ans)
    q -= 1
