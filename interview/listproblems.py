# # LIST PROBLEMS
# # 🟢 Level 1 – Basics

# # Find the largest and smallest element in a list.
# # ls=[1,5,8,2,3,9,4]
# # large=-float("Inf")
# # small=float("Inf")
# # for i in ls:
# #     if i>large:
# #         large=i
# #     if i<small:
# #         small=i
# # print(small,large)
    
# # Count even and odd numbers in a list.
# # l=[1,2,4]
# # even=0
# # odd=0
# # for i in l:
# #     if i & 1==0:
# #         even+=1
# #     else:
# #         odd+=1
# # print(even,odd)
# # Reverse a list without using reverse().
# # l=[1,2,3,4]
# # new=[]
# # for i in range(len(l)-1,-1,-1):
# #     new.append(l[i])
# # print(new)
# # Remove duplicates from a list.
# # l=[1,1,2,3]
# # new=[]
# # for i in l:
# #     if i not in new:
# #         new.append(i)
# # print(new)
    
# # Find the sum and average of list elements.
# # l=[1,2,3,4]
# # sum=sum(l)
# # avg=sum/len(l)
# # print(sum,avg)


# # 🟡 Level 2 – Logic & Patterns

# # Find the second largest element.

# # Rotate a list by k positions.
# # a = [1, 2, 3, 4, 5]
# # k = 3
# # n = len(a)
# # #  a[(i - k) % n]
# # -2%5
# # print(-2 % 5)

# # k=0
# # new=[]
# # print(len(l)-k-1)

# # for i in range(len(l)-k-1):
# #     new.append(l[len(l)-1-i])
# # for i in range(k+1):
# #     new.append(l[i])
# # print(new)
# # Check if a list is a palindrome.
# # l=[1,2,3,2,1]
# # if l==l[::-1]:
# #     print("palindrome")
# # Merge two lists alternately.
# # l1=[1,3,5,7]
# # l2=[2,4,6,8]

# # for i,j in zip(l1,l2):
# #     new.append(i)
# #     new.append(j)
# # print(new)

# # Find missing number from 1 to N.
# # l=[1,2,4,5]
# # for i in range(1,len(l)):
# #     if l[i]-l[i-1]==2:
# #         print(l[i-1]+1)
# # 🔵 Level 3 – Recursion + Nested Lists

# # Flatten a nested list using recursion.
# # l=[1, [2, 3], [4, [5, 6]], 7]
# # # a=[[1, 2], [3, [4, [5]]]]
# # new=[]
# # def flatten(a):
# #     for i in a:
# #         if type(i)==list:
# #             flatten(i)
# #         else:
# #             new.append(i)
# #     return new


# # xx=flatten(l)
# # print(xx)


# # Find the sum of all elements in a nested list.
# # l=[1, [2, 3], [4, [5]], 6]

# # sum=0
# # def flat(ls):
# #     for i in ls:
# #         if type(i)==list:
# #             flat(i)
# #         else:
# #             sum+=i

# # flat(l)
# # print(sum)
# # Find maximum element in a nested list (recursive).
# # la=[3, [9, 1], [4, [15, 2]]]
# # haha=0
# # k=[]
# # for i in la:
# #     if type(i)==list:
# #         if len(i)>haha:
# #             haha=len(i)
# #             k=i
# # print(haha,k)
    
# # Count total elements (including nested ones).

# # Reverse a list using recursion.

# # 🟣 Level 4 – Scenario Based

# # Student marks list → find topper and average.

# # E-commerce cart prices → calculate total bill.

# # Attendance list → find absentees.

# # Daily expenses → find highest spending day.

# # Scores list → remove outliers (very high/low).

# # def flatten(lst):
# #     res = []
# #     for i in lst:
# #         if type(i) == list:
# #             res.extend(flatten(i))
# #         else:
# #             res.append(i)
# #     return res

# # print(flatten([1, [2, 3], [4, [5, 6]], 7]))

# # def nested_sum(lst):
# #     total = 0
# #     for i in lst:
# #         if type(i) == list:
# #             total += nested_sum(i)
# #             print(total)
# #         else:
# #             total += i
# #     return total

# # print(nested_sum([1, [2, 3], [4, [5]], 6]))


# # scores = [45, 48, 50, 47, 200, 49, 46]

# # clean = []
# # for s in scores:
# #     if s < 100:
# #         clean.append(s)

# # print(clean)

# # marks = [78, 85, 92, 66, 88]

# # topper = marks[0]
# # total = 0

# # for m in marks:
# #     if m > topper:
# #         topper = m
# #     total += m

# # average = total / len(marks)

# # print("Topper:", topper)
# # print("Average:", average)

# # a = 5
# # def modify(x):
# #     x = x + 10
# #     print(x)

# # print(a)
# # modify(a)

# # def freet():
# #     print("teja")

# # def greet(a):
# #     a()
# # greet(freet)
# # print(2 and 1)
# print( 2| 4)


# def outer(fun):
#     def inner():
#         print("Hello from 1")
#         fun()
#         print("Hello from 2")
#     return inner

# @outer
# def teja():
#     print("middle")
    
# teja()


# def greet():
#     print("hello sir")

# def cheppu(param):
#     param()
# cheppu(greet)



# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before function")
#         result=func(*args, **kwargs)
#         print(result)
#         print("After function")
#     return wrapper

# @decorator
# def add(a, b):
#     return a + b

# add(5, 3)

# x = 10

# def func():
#     global x
#     x = 20
# func()
# print(x)

# test_math.py

# try:
#     num = int(input("Enter number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except ValueError:
#     print("Invalid input")

