# input=[3,7,2,9,5]
# a=0
# for i in input:
#     if i>a:
#         a=i
# print(a)

# arr = [1, 2, 3, 4, 5]
# target = 6
# count=0
# for i in arr:
#     for j in arr:
#         if i+j==target:
#             count+=1
# print(count)

# Input=[1, 3, 4, 2, 2]
# count=0
# for i in range(len(Input)):
#     for j in range(i+1,len(Input)):
#         if Input[i]==Input[j]:
#             count=Input[j]
# print(count)

# 4. Count pairs with difference = k
# arr=[1,5,3,4,2]
# k=2 # -> 3
# count=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if abs(arr[i]-arr[j])==k:
#             count+=1
# print(count)

# 7. Find all duplicates

# arr=[1,2,3,2,4,1]
# # a=[1,2]
# empty=[]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             empty.append(arr[i])
# print(empty)

# MEDIUM–HARD (Brain stretch)
# 10. Check if any triplet sum = target

# arr=[1,2,3,4,5]
# target=9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             if arr[i]+arr[j]+arr[k]==target:
#                 # print(True)
#                 print(arr[i],arr[j],arr[k])
# 👉 (1+3+5, 2+3+4)

# lambda function: it is a single lined nameless function
# It's short and simple , used for mathematical operations
# used in Higher order functions

# syntax: square= lambda arguments : expression

# multiply=lambda a,b:a+b
# print(multiply(2,3))

# def multiply(a,b):
#     return a*b
# print(multiply(1,2))

# multiply=lambda a,b:a*b
# print(multiply(1,2))

# 2. map() apply function to all items

# plus 2 for everyitem ( +2 )
# a=[1,2,3,4]

# for i in range(len(a)):
#     a[i]+=2
# print(a)

# syntax for map
# map(function,iterable)
# print(function)

# nums=[11,12,10,9,8]
# filtered=list(filter(lambda x:x>10,nums))
# squares=list(map(lambda x:x**2,filtered))
# print(squares)
# result=list(map(lambda x :x**2,filter(lambda x:x>10,nums)))
# print(result)
# result=map(lambda x:x+1,nums)
# print(list(result))

# def add2(nums):
#     return nums+1

# result=list(map(add2,nums))
# print(result)

# a=lambda x:x+2

# ar=[1,2,3]
# m=list(map(a,ar))
# print(m)

# def even(nums):
#     if nums%2==0:
#         return False
#     return True

# x=list(filter(even,nums))
# print(x)

# x=list(filter(lambda x:x%2==0,nums))
# print(x)

# words = ["hi", "hello"]
# x=list(map(lambda x:x.upper(),words))
# print(x)

# print("abc".upper())

# abc=input().split()
# x=[]
# for i in abc:
#     x.append(int(i))
# freq={}
# for i in x:
#     freq[i]=freq.get(i,0)+1

# max_as=max(freq.values())
# m=[i for i,j in freq.items() if j==max_as]
# print(m[0])

# a=eval(input("enter list: "))
# print(type(a))
# a=input("enter: ").strip("[]?").split(",")

# result=list(map(lambda x:int(x),a))
# print(result)

# def add(*args):
#     print(1,2)

# add(1, 2, 3)

# multi positional and KeyWord arguments,

# def key(**kwargs):
#     for i,j in kwargs.items():
#         print(i,":",j)

# key(name="teja",agee=21)

# asd={(1,2):"asd",
#      ("i,"):"aa"}
# print(asd)

# Create function to find maximum using *args

# def findmax(*arg):
#     return max(arg)
# x=findmax(1,2,3,4)
# print(x)

# def dic(**kwargs):
#     return kwargs
# x=dic(name="raviteja",age=21)
# print(x)

# ✅ Problem 1: Sum of even numbers

# Using *args, return sum of only even numbers

# input: add(1,2,3,4,5,6)
# def check(*arg):
#     sum=0
#     for i in arg:
#         if i%2==0:
#             sum+=i
#     return sum

# inputs=(1,2,3,4,5,6)
# result=sum(filter(lambda x:x%2==0,inputs))
# print(result)
# output: 12  (2+4+6)

# def show(**kwarg):
#     for i in kwarg:
#         if i[0]=='a':
#             print(i)
    
# show(name="Ravi", age=22, address="Hyd")

# d={"name":"Ravi", "age":22, "address":"Hyd"}
# for i in d:
#     if i.startswith("a"):
#         print(i)
# nums=[1,2,3,4]
# print(type(*nums))
# def add(*nums):
#     print(nums)
# add(*nums)

# Random & Math
import random
# a=random.randint(0,100)
# print(a)

nums=[]
# while len(nums)<100:
#     a=random.random()*100
#     if a not in nums:
#         nums.append(int(a))
# print(nums)
# while len(nums)<20:
#     a=random.random()*91
#     if int(a) not in nums:
#         nums.append(int(a))
# print(nums)
    # print(int(a))
# print(random.randrange(1, 10, 9))
nums = [1, 2, 3, 4, 5]
print(random.sample(nums, 3))
 
    
# nums = [1, 2, 3, 4]
# random.shuffle(nums)
# # print(nums)
# for i in range(len(nums)):
#     print(nums[i],i)

