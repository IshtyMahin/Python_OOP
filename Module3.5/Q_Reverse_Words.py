# s = list(input().split(" "))

# for i in range(len(s)-1):
#     str = s[i]
#     print(str[::-1],end=" ")
    
# str = s[len(s)-1]
# print(str[::-1])
    

   
words = input().split(" ")

reversed_words = [word[::-1] for word in words[:-1]]
reversed_words.append(words[-1][::-1])


result = " ".join(reversed_words)

print(result)
