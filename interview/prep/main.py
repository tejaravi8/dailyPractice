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

abc="abcacccbb"
chars=set()
left=0
max_length=0

for right in range(len(abc)):
    while abc[right] in chars:
        chars.remove(abc[left])
        left+=1
    chars.add(abc[right])
    max_length=max(max_length,right-left+1)
    print(max_length,right,left)