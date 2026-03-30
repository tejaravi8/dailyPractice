# Check if number is palindrome

# a=12345
# reverse=""
# for i in str(a):
#     reverse=i+reverse
# print(reverse)

# a=12345
# reverse=""
# for i in (str(a)):
#     reverse=i+reverse
# print(reverse)
# a=a = [10, 5, 20, 8, 15] #[10,5,20,8]
# first=second=-float("inf")
# for i in a:
#     if i>first:
#         second=first
#         first=i
#     elif i < first and i > second:
#         second=i
# print(second)


# abc=[1, 2, 2, 3, 4, 4]
# output=[]
# for i in abc:
#     if i not in output:
#         output.append(i)
# print(output)

# 3. First Non-Repeating Character
# abc="aabbcde"
# non={}
# c=0
# for i in abc:
#     if i not in non:
#         non[i]=1
#     else:
#         non[i]+=1
# for i in non:
#     if non[i]==1 and c<1:
#         print(i)
#         c+=1
#         # break

# abc="hello world".split()
# word=""
# rev=""
# for i in abc:
#     word+=i[::-1]
#     rev=rev+word+" "
#     word=""
# print(rev)

# input=[1, 2, 2, 3]
# qbc={}
# for i in input:
#     qbc[i]=qbc.get(i,0)+1
# print(qbc)
# input= [0,1,0,3,12]
# # Output: [1,3,12,0,0]
# q=[]
# a=[]
# for i in input:
#     if i !=0:
#         q.append(i)
#     else:
#         a.append(i)
# array=q+a
# print(array)

# input="MAdam"
# abc=input.lower()
# rev=""
# for i in abc:
#     rev=i+rev
# print(rev==abc)

# Input=[1,2,4,5]

# for i in range(1,len(Input)):
#     if Input[i]-Input[i-1]==2:
#         print(Input[i]-1)
        
# Input = [-2,1,-3,4,-1,2,1,-5,4]

# max_sum=Input[0]
# current_sum=Input[0]

# for i in range(1,len(Input)):
#     current_sum=max(Input[i],current_sum+Input[i])
#     max_sum=max(current_sum,max_sum)
# print(max_sum)

# find missing number from 1 to n
# num_list=[2,3,4,6]

# total=list(range(min(num_list),max(num_list)+1))
# for i in total:
#     if i not in num_list:
#         print(i)
# n=len(nums)+1
# s=sum(nums)
# missing= int(n*(n+1)/2) - s
# print(missing)
# num_list=set(num_list)
# expected_range = list(range(min(num_list), max(num_list) + 1))
# for i in expected_range:
#     if i not in num_list:
        # print(i)
# print(expected_range)
# print(expected_range)
# def find():
#     for i in expected_range:
#         if i not in num_list:
#             return i
# x=find()
# print(x)

# abc = [0,1,0,3,0,12]
# j=0
# for i in range(len(abc)):
#     if abc[i]>0:
#         abc[j],abc[i]=abc[i],abc[j]
#         j+=1
# print(abc)

# [1,2,2,4,5] → Missing = 3, Repeating = 2
# abc = [1,2,2,4,5]
# bv=set(abc)
# total=list(range(min(abc),max(abc)+1))
# for i in total:
#     if i not in bv:
#         print(i)

# freq={}
# for i in abc:
#     freq[i]=freq.get(i,0)+1
# for i in freq:
#     if freq[i]>1:
#         print(f"repeating {i} in {freq[i]} times")

# abc=123456
# sum=0
# while abc>0:
#     check=abc%10
#     if check%2==0:
#         sum+=check
#     abc//=10
# print(sum)

# Find the longest substring without repeating characters

# Input: "abcabcbb"
# Output: 3 ("abc")

# abc="abcacccbb"
# chars=set()
# left=0
# max_length=0

# for right in range(len(abc)):
#     while abc[right] in chars:
#         chars.remove(abc[left])
#         left+=1
#     chars.add(abc[right])
#     max_length=max(max_length,right-left+1)
#     print(max_length)


# s = "accabac"
# char_set = set()
# left = 0
# max_length = 0
# longest_substring = ""
# for right in range(len(s)):
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left+=1
#     char_set.add(s[right])
#     current = s[left:right+1]
#     if len(current)>max_length:
#         max_length=len(current)
#         longest_substring=current
# print(max_length,longest_substring)
        
# for right in range(len(s)):
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left += 1
#     char_set.add(s[right])
#     # current substring
#     current = s[left:right+1]
#     if len(current) > max_length:
#         max_length = len(current)
#         longest_substring = current
# print("Length:", max_length)
# print("Substring:", longest_substring)

# Given an array, find the maximum subarray sum

# num=6 # 1, 2, 3, 4, 5, 6
# totle=0
# for i in range(1,num//2+1):
#     if num%i==0:
#         totle+=i
# print(totle)

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# max_sum=arr[0]
# current_sum=arr[0]

# for i in range(len(arr)):
#     if arr[i]>current_sum+arr[i]:
#         current_sum=arr[i]
#         temp=i
#     else:
#         current_sum+=arr[i]
#     if current_sum>max_sum:
#         max_sum=current_sum
#         start=temp
#         end=i
# print(arr[start:end+1])

# for i in range(1,len(arr)):
#     if arr[i]>current_sum+arr[i]:
#         current_sum=arr[i]
#         temp=i
#     else:
#         current_sum+=arr[i]
    
#     if current_sum>max_sum:
#         max_sum=current_sum
#         start=temp
#         end=i

# print(max_sum,"Max_sum")
# print("Subarray",arr[start:end+1])

#     current_sum=max(arr[i],arr[i]+current_sum)
#     max_sum=max(current_sum,max_sum)
# print(max_sum)

# longest substring

# s="abcccbcbab"
# chars=set()
# left=0
# max_length=0

# for right in range(len(s)):
#     while s[right] in chars:
#         chars.remove(s[left])
#         left+=1
#     chars.add(s[right])
#     max_length=max(max_length,right-left+1)
# print(max_length)

# abc="Count number of words in a sentence".split()
# print(len(abc))

# abc="Count number of words in a sentence"
# l=[]
# word=""
# for i in abc:
#     if i !=" ":
#         word+=i
#     else:
#         l.append(word)
#         word=""
# l.append(word)
# print(l)

# # Given an array, find all duplicates

# # Input: [1,2,3,2,4,1]
# # Output: [1,2]

# abc= [1,2,3,2,4,1]
# b=set()
# dup=[]
# for i in abc:
#     if i not in b:
#         b.add(i)
#     else:
#         dup.append(i)
# print(dup)

# Find first repeating element in array

# Input= [10,5,3,4,3,5,6]
# l=set()
# for i in Input:
#     if i not in l:
#         l.add(i)
#     else:
#         print(i)
#         break
# # Output: 3

# num1=13
# num2=26
# x=1
# for i in range(2,num1+1):
#     if num1%i==0 and num2%i==0:
#         x=i
# print(x)

# # freq1={"a":1,"b":2,"c":3}
# # freq2={"b":2,"c":5,"a":1}
# from collections import Counter
# freq1 = "listen"
# freq2 = "silent"
# # print(sorted(freq2))
# s1=Counter(freq1)
# s2=Counter(freq2)+Counter("s")
# print(s1,s2)

# arr = [1,2,3,4,5]
# k=6
# k=k%len(arr)

# result=arr[-k:]+arr[:-k]
# print(result)

# a="aabbcc"
# new=""
# count=1
# for i in range(1,len(a)):
#     if a[i]==a[i-1]:
#         count+=1
#     else:
#         new+=str(a[i-1])+f"{count}"
#         count=1
# new+=str(a[len(a)-1])+f"{count}"
# print(new)

# Check Rotation of String

# 👉 "abcde" and "cdeab" → YES
# a1="abcde"
# a2="cdeab"
# freq1,freq2={},{}
# for i in a1:
#     freq1[i]=freq1.get(i,0)+1
# for j in a2:
#     freq2[j]=freq2.get(j,0)+1
# print(freq1==freq2)

# input="I love coding".split()
# new=""
# for i in reversed(input):
#     new+=i+" "
# print(new)

# second smallest
# nums=[3,1,5,2,7,12,35,22,2]
# first=float("inf")
# second=first
# third=first
# for i in nums:
#     if i<first:
#         third=second
#         second=first
#         first=i
#     elif i>first and i<second:
#         third=second
#         second=i
#     # elif i>second and i<third:
#     #     third=i
    
# print(third,second)
# # for i in nums:

# Leader array

# abc=[1, 2, 3, 4, 5, 2]

# leaders=[]
# max_num=abc[-1]
# leaders.append(max_num)

# for i in range(len(abc)-2,-1,-1):
#     if abc[i]>max_num:
#         max_num=abc[i]
#         leaders.append(max_num)
# print(leaders[::-1])

# 🚀 Q7: Equilibrium Index
# arr=[1,3,5,2,2]
# # 13 -1=12  1
# # 12-3=9    4
# # 9-5=4
# # 4-2=2
# # 2-2=0
# # 
# # arr = [1,3,5,2,2]
# # total = sum(arr)
# # left_sum = 0

# # for i in range(len(arr)):
# #     total-=arr[i]
# #     if total==left_sum:
# #         print(i)
# #         break
# #     left_sum+=arr[i]

# a = [1,3,5]
# b = [2,4,6]

# i=j=0
# merged=[]
# # merged.extend(a)
# # merged.extend(b)
# # merged.sort()
# # print(merged)
# while i<len(a) and j<len(b):
#     if a[i]<b[j]:
#         merged.append(a[i])
#         i+=1
#     else:
#         merged.append(b[j])
#         j+=1
# # merged.extend(a[i:])
# # merged.extend(b[j:])
# # print(merged,i,j)

# a = [1,2,3,4]
# b = [3,4,5,6]
# a=set(a)
# b=set(b)
# print(a-b)
# print(list(set(a)&set(b)))

# s = "thequickbrownfoxjumpsoverthelaydzog"

# alphabets = set("abcdefghijklmnopqrstuvwxyz")
# print(alphabets)
# print(len(alphabets))

# if alphabets.issubset(set(s.lower())):
#     print("Pangram")
# else:
#     print("Not Pangram")
# l=set(s.lower())
# print(len(l))

# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5, 6}
# set_c = {1, 2, 6}

# # print(f"Using .issubset(): {set_a.issubset(set_b)}") 
# # print(f"Is set_c a subset of set_b?: {set_c.issubset(set_b)}")

# s = "thequickbrownfoxjumpsoverthelazydog"
# alphabets=set("abcdefghijklmnopqrtuwxyz")
# x=alphabets.issubset(set(s))
# print(x)

# s = "aeiouuabc"

# vowels = set("aeiou")
# count = 0
# current = 0

# for ch in s:
#     if ch in vowels:
#         current += 1
#         count += current
#         print(count)
#     else:
#         current = 0

# print(count)

