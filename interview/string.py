# s=['o', 'l', 'l', 'e', 'h']
# print(list(reversed(s)))

# 1️⃣ Reverse a String
# s="hello"
# print(list(reversed(s)))

# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)

# s=list(s)
# left = 0
# right=len(s)-1

# while left < right:
#     s[left],s[right]=s[right],s[left]
#     left+=1
#     right-=1

# print("-".join(s))

# s = "maddam"
# is_palindrome=True
# if s[::-1] !=s:
#     is_palindrome=False
# print(is_palindrome)

# left=0
# right=len(s)-1
# is_palindrome=True
# while left<right:
#     if s[left] !=s[right]:
#         is_palindrome=False
#     left+=1
#     right-=1
# print(is_palindrome)
# vowels = set("aeiou")

# print(vowels)

# s={'o', 'e', 'a', 'u', 'i'}
# s="aeiou"
# which check is more good for membership "a" in s

# s1 = "potss"
# s2 = "stop"

# print(sorted(s1)==sorted(s2))
# is_ana=True
# if len(s1) !=len(s2):
#     is_ana=False

# freq={}
# for i in s1:
#     freq[i]=freq.get(i,0)+1

# for j in s2:
#     if j not in freq:
#         is_ana=False
#         break
#     freq[j]-=1

# print(freq)
# print(list(value==0 for value in freq.values()))

# print(is_ana)

# s="swiss"
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# for i in s:
#     if d[i]==1:
#         print(i)
#         break

# s="banana"
# f=[]
# for i in s:
#     if i not in f:
#         f.append(i)

# for i in f:
#     j="".join(f)
# print(j)

# person = {"name": "Alice", "age": 30}
# print(len(person))

# s="abcabcabc"
# s = "abb"

# left=0
# window=set()
# max_len=0

# for right in range(len(s)):
#     while s[right] in window:
#         window.remove(s[left])
#         left+=1
#     window.add(s[right])
#     max_len=max(max_len,right-left+1)

# print(max_len,window)

# s = "abb"

# left = 0
# window = set()
# max_len = 0
# start = 0   # start index of longest substring

# for right in range(len(s)):
#     while s[right] in window:
#         window.remove(s[left])
#         left += 1

#     window.add(s[right])

#     if right - left + 1 > max_len:
#         max_len = right - left + 1
#         start = left   # store where this best window started

# print(s[start:start + max_len])

# a=[1,2,3]
# print(id(a))
# a.append(4)
# print(id(a))

# immutable has fixed memory address.
# if we try to change the immutable ones ,
# the memory adress get changed

# d=(1,2,3)
# print(id(d))
# d=list(d)
# print(id(d))
# d.append(4)
# print(id(d))
# d=tuple(d)
# print(id(d))

# d={1,2,3}
# print(id(d))
# d.add(4)
# print(id(d))

# d={'a':1,"b":2}
# print(id(d))
# d['c']=1
# #  check if it override or ignore over adding elements in dictionary
# # regology question

# print(d)
# print(id(d))

# d={"a":2,"b":"10k"}
# d["a"],d["b"]=d["b"],d["a"]
# print(d)

# d=[{"a":1,"b":"10k"},{"a":None,"b":"vc"},{"a":3,"b":None}]
# for i in d:
#     if type(i["a"]) !=int:
#         i["a"]=0
#     if type(i["b"])!=str:
#         i['b']="string"
# print(d)

# print({1:"teja"})

# print("qwe")

# arr = [12,-1,-7,8,-15,30,16,28]
# k = 3
# output=[]
# l=len(arr)
# for i in range(l):
#     left=0
#     while left<k and arr[i]<0:
#         output.append(arr[i])
        
# print(output)

# s="abb"
# left=0
# seen=set()
# max_len=0
# st=0
# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left+=1
#     seen.add(s[right])
#     if max(max_len,right-left+1)==right-left+1:
#         max_len=right-left+1
#         st=left
# print(s[st:st+max_len])

