# # # # create

# # # s={3,4,6,7,8,9}

# # # # s.add(4)
# # # # s.add(3)


# # # # for i in s:
# # # #     print(i)


# # # # s.add(9)
# # # # s.update()
# # # s.pop()
# # # print(s)

# # d = {"name": "Teja", "age": 22}

# # # d["city"] = "Hyd"
# # # d.update({"lang": "Python"})
# # # print(d)


# # d.get("age")

# # d.popitem()

# # # d.clear()

# # d.pop("name")

# # print(d)

# 🔥 20 Random Python Problems
# 1. List – Replace all even numbers with "EVEN"

# Input:

# nums=[10, 21, 32, 43, 54]
# new=[]
# for i in nums:
#     if i%2==0:
#         new.append("EVEN")
#     else:
#         new.append("ODD")

# print(new)
# Output:
# ["EVEN", 21, "EVEN", 43, "EVEN"]

# 2. Dictionary – Count how many students passed

# pass >= 40

# data={"ram": 55, "teja": 30, "ravi": 70}
# # count=0
# for i,j in data.items():
#     if j>40:
#         count+=1
        
# print(count)


# 3. Set – Remove duplicates from a list (without set())

# data=[1,2,3,4,5,6,4,3,7,2]
# new=[]
# dup=[]
# for i in data:
#     if i not in new:
#         new.append(i)
#     else:
#         dup.append(i)
        
# print(dup)


# Solve using loops only.

# 4. Tuple – Convert tuple of numbers into list and add 100 to each element

# Input:

# nums=(2, 4, 6)
# nums=list(nums)
# for i in range(len(nums)):
#     nums[i]+=100

# print(tuple(nums))
    

# 5. String – Count vowels in a string

# Input:

# name="tejaravi"
# for i in name:
#     if i not in "aeiou":
#         print(i)

# 6. CRUD – Insert an item at index 2 in a list without using insert()
# a=[1,2,3,4,5]
# a=a[:2]+[0]+a[2:]
# print(a)
# 7. Dictionary – Convert two lists into a dictionary

# Example:

keys = ["name", "age", "city"]
values = ["Teja", 22, "Hyd"]
dic={}
# dic.update(zip(keys,values))
# print(dic)

# for i,j in zip(keys,values):
#     dic[i]=j
# print(dic)

# 8. List – Find the second largest number
nums=[1,4,6,9,-9,7,3]
# first=second=float("-inf")

# for i in nums:
#     if i>first:
#         second=first
#         first=i
#     elif first>i and i>second:
#         second=i

# print(second)

# first=second=float("inf")

# for i in nums:
#     if i<first:
#         second=first
#         first=i
#     elif first<i and i<second:
#         second=i

# print(second)
# Do NOT use sorted().

# 9. Tuple – Find index of element WITHOUT using .index()
data=(1,2,3,4,5,6,7)
# for i,j in enumerate(data,start=0):
#     print(i,j)

# print(data.index(1))


# 10. Set – Check if two sets are disjoint (no common elements)
# a={1,2,3,4,5,6}
# b={7,8}
# print(a.isdisjoint(b))
# Try to solve without using built-in methods.

# 11. String – Reverse a string without slicing ([::-1])
# 12. Dictionary – Merge two dictionaries manually

# Do not use update().

# 13. List – Move all zeros to the end

# Input:

# [0, 1, 0, 3, 12]


# Output:

# [1, 3, 12, 0, 0]

# 14. Tuple – Count how many times a value appears without using .count()
# 15. Set – Find common elements between 3 sets
# 16. String – Remove all special characters

# Input:

# "he!!o@wor#ld"


# Output:

# "helloworld"

# 17. Dictionary – Swap keys and values of a dictionary

# Input:

# {"a": 1, "b": 2}


# Output:

# {1: "a", 2: "b"}

# 18. Loop – Print numbers from 1 to 100 but skip multiples of 5
# 19. List – Create a new list with squares of numbers

# Input:

# [2, 3, 4]


# Output:

# [4, 9, 16]

# 20. Logic – Check if a number is prime