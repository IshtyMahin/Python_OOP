# n = int(input())
# s = input()

# sum=0
# for i in range(n):
#     sum+= int(s[i])

# print(sum) 


n = int(input())
s = input()

total_sum = sum(int(char) for char in s)
print(total_sum)
