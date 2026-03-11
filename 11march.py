# # # Data structures
# # a=(1,2,3,4)
# # a[0]=1
# # print(a)   # type error : tuple object does not support item assignment

# # a.remove(1)
# # a.append(1)
# # a.pop(0)
# # a.sort()
# # a.reverse()
# # for i in reversed(a):
# #     print(i)
# # print(a)
# # a="string"
# # new=reversed(a)
# # print(tuple(new))
# # print(a)
# # a.reverse()
# # print(a)
# # print
# # print(a)
# # print(a)
# # a.insert(4,100)
# # print(a[4])

# # tuple
# # a=(1,2,3,4)
# # print(a.count(1))

# # unpacking
# # a=(1,2,3,4)
# # x,y,z,k=a

# # set
# # a={1,2,3,4}
# # b={1}
# # x=b.difference(a)
# # x=a.union(b)
# # x=a.intersection(b)
# # x=a.isdisjoint(b) no values common between them # issubset() subset is a part of super set or not , issuperset() super set contains the subset or not
# # a.add("s")
# # a.discard(7)   #it leaves if item not found
# # a.remove(8)   # it through an keyError if not found the object/item
# # print(x)

# # methods
# # list : append(),pop(),insert(),remove(),sort(),reverse(), len() built in function
# # tuple : accessing ,through indexing
# # set : add(),issubset(),issuperset(),union(),intersection(),remove(),discard()
# # dictionary : keys(),values(),items(),update()
# # ab={"x":1,"b":2}
# # x=ab.get("a","Not found")
# # print(x)

# # a=[1,2,3,7,9]
# # b=[5,6,7,8,7]
# # zipped=zip(a,b,strict=True)
# # print(list(zipped))
# # aaa={'a': 1, 'b': 2}
# # # for i in a.values():
# # #     print(i)

# # pairs = [('A', 1), ('B', 2)]
# # letters, numbers = zip(*pairs)
# # print(numbers)

# # j=[1,1,1,1,1,1]
# # # j=[x for x in j if x!=1]
# # # print(j)

# # for i in range(len(j)-1,-1,-1):
# #     if j[i]==1:
# #         j.pop(i)
# # print(j)

# # numbers = [1,2,3,4,5,6]
# # evens=[x for x in numbers if x%2!=0]
# # print(evens)

# contacts = {}  # Our accumulator (starts empty)

# while True:
#     print("\n--- Contact Manager ---")
#     print("1. Add Contact  2. View All  3. Search  4. Exit")
#     choice = input("Choose an option: ")

#     if choice == '1':
#         name = input("Enter Name: ").strip().title()
#         phone = input("Enter Phone: ").strip()
#         contacts[name] = phone  # Accumulating data
#         print(f"Added {name}!")

#     elif choice == '2':
#         print("\nAll Contacts:")
#         for name, phone in contacts.items():
#             print(f"{name}: {phone}")

#     elif choice == '3':
#         search = input("Search Name: ").strip().title()
#         # Using .get() to avoid errors if name isn't found
#         result = contacts.get(search, "Contact not found.")
#         print(f"Result: {result}")

#     elif choice == '4':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice, try again.")

# CLI To-Do Application
# tasks={}
# tasknum=1
# while True:
#     print(
# """
# 1.Add task 
# 2.View tasks 
# 3.Delete task 
# 4.Save task in files
# """)
#     a=int(input("\nchoose option: "))
#     if a==1:
#         task=input("enter task here: ")
#         tasks[tasknum]=task
#     if a==2:
#         print("""
# --------TASKS------------""")
#         for i in tasks:
#             print(tasks[i])
#         print("-------------------------")
#     if a==3:
        
# 
# a=[1,2,3]
# b=a
# b.append(4)
# print(a) # refers to sam ememory location

# print(a is b) # if b=[1,2,3] instead of b=a it is False

# datatype tells the type of value a variable reffering to

# --- LIST (Mutable) ---
# my_list = [1, 2]
# print(id(my_list))
# my_list.extend([3])
# print(id(my_list))
# original_list_id = id(my_list)

# my_list =my_list+ [3]  # Modifies the existing list in place

# print(f"List: {my_list}")
# print(f"Same object? {id(my_list) == original_list_id}") # Returns True


# # --- TUPLE (Immutable) ---
# my_tuple = (1, 2)
# original_tuple_id = id(my_tuple)

# my_tuple += (3,) # Creates a brand new tuple and reassigns the name

# print(f"Tuple: {my_tuple}")
# print(f"Same object? {id(my_tuple) == original_tuple_id}") # Returns False

# Why functions next?

# Because interviewers LOVE asking:

# How arguments are passed in Python

# Why lists change inside functions but integers don’t

# Output-based questions (traps 😈)

# All of this depends on:
# 👉 mutable vs immutable (which you now understand)

# def check():
#     return "abab"
# check()

# function is a reusable block of code used to perform a particular task

# def gen():
#     yield 1
#     yield 2
#     yield 3


# g=gen()
# # print(next(g))
# # print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# a=[1,2]

# it=iter(a)
# try:
#     print(next(it))
#     print(next(it))
#     print(next(it),"ho")
#     print(next(it),"hi")
# except StopIteration:
#     print("stopIterationg")
# from collections import Counter
# x=[1,1,2,3,2,1]
# freq={}
# for i in x:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)
# # Counter(x)
# print(dict(Counter(x)))
# Output:
# 1:3
# 2:2
# 3:1

# di={"a":5,"b":10,"c":3}
# maximum=0
# output=0
# for i in di:
#     if di[i]>maximum:
#         maximum=di[i]
#         output=i
# print(output)

# Output: b

# prime function
# def prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
# x=prime(12)
# print(x)

# Write a function to find factorial.
# def factorial(num):
#     number=1
#     if num<2:
#         return 1
#     for i in range(2,num+1):
#         number=number*i
#     return number
# x=factorial(0)
# print(x)

# Write a function to return largest element in list.
# def findmax(nums):
#     return max(nums)

# list=[2,7,4,9,1,45,33,77,44,7,69,8]
# x=findmax(list)
# print(x)

# def cnt(sentence):
#     return len(sentence.split())
    
# x=cnt("hello all of you")
# print(x)

# a="listen"
# b="silent"
# print(sorted(a)==sorted(b))