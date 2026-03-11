# # # numbers=[]
# # # for i in range(1,4):
# # #     num=int(input(f"enter number {i}: "))
# # #     numbers.append(num)
# # # print(f"Largest number is {max(numbers)}")

# # # Student Marks Calculator

# # # Program should:

# # # Ask student name
# # # Ask marks of 3 subjects
# # # Calculate total
# # # Calculate average
# # # Print grade

# student_name=input("enter Student name : ")
# maths=int(input("enter Math marks: "))
# physics=int(input("enter Physics  marks: "))
# english=int(input("enter English marks: "))
# total=maths+physics+english
# average=total/3
# if average>90 and average<=100:
#     grade="A+"
#     print(f"\nExcellent performance {student_name}!")
# elif average>80 and average<=89:
#     grade="A"
# elif average>60 and average<=79:
#     grade="B"
# else:
#     grade="pass"

# # print(f"""
# # ----------------------------------
# # Enter student name: {student_name}
# # Math marks: {maths}
# # Science marks: {physics}
# # English marks: {english}

# # Total = {total}
# # Average = {average}
# # Grade = {grade}
# # ----------------------------------
# # """)

# # number guessing game
# import random

# number=random.randint(0,100)
# attempts=0
# while True:
#     num1=int(input("enetr number: "))
#     if num1>number:
#         print("high")
#         attempts+=1
#     elif num1<number:
#         print("low")
#         attempts+=1
#     else:
#         attempts+=1
#         print(f"correct {number}, in {attempts}attempts")
#         break

# number=int(input("enter number: "))
# for i in range(1,11):
#     print(f"{number} * {i} = {number*i}")

# n=5
# for i in range(1,n+1):
#     print("* "*i)

# n=5
# for i in range(n):
#     print("* "*(n-i))

#          *
#        * *
#      * * *
#    * * * *
#  * * * * *

# n=5
# for i in range(n):
#     print("  "*(n-i) + " *"*i)

# # n=5
# for i in range(n):
#     print("  "* i + " *" * (n-i))

# n=5
# for i in range(1,n):
#     print(" *"*i+"  "*(n-i)+"  "*(n-i)+" *"*i)
# for i in range(n):
#     print(" *"*(n-i)+ "  "*i+"  "*i+" *"*(n-i))

# n=5
# for i in range(n):
#     print("  "*i + " *"*(n-i-1)+" *"*(n-i))

# def add(a,b):
#     return sum([a,b])
# x=add(5,6)
# print(x)

# def claculator(a,b,problem):
#     if problem =="add":
#         return a+b
#     if problem =="sub":
#         return a-b
#     if problem =="mul":
#         return a*b
#     if problem =="div":
#         return a/b
# problem=claculator(50,15,'sub')
# print(problem)

