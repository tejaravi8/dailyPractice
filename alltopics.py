# 🟢 LEVEL 1 — Basics (Must be perfect)

# Reverse a string without using slicing

# name="racecar"
# rev=""
# for i in name:
#     rev=i+rev
# print(rev)

# Check whether a number is prime
# number=15
# def check_prime(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# x=check_prime(number)
# print(x)
# Find the largest and smallest element in a list (no built-ins)
# l=[1,2,3,4,5,6]
# maximum=l[0]
# minimum=l[0]
# for i in l:
#     if i>maximum:
#         maximum=i
#     if i<minimum:
#         minimum=i
# print(maximum,minimum)
# Count vowels in a string
# name="raviteja"
# vowels="aeiou"
# cou=0
# for i in name:
#     if i in vowels:
#         cou+=1
# print(cou)
# Swap two numbers without using a third variable

# Check whether a string is a palindrome
# st="dad"
# rev=""
# for i in st:
#     rev=i+rev
# if st==rev:
#     print("yes")
# else:
#     print("no")
# Sum of digits of a number
# number=343
# temp=number
# summ=0
# while temp>0:
#     summ+=temp%10
#     temp//=10
# print(summ)
# Find factorial using a function
# num=5
# def factorial(num):
#     if num<2:
#         return 1
#     else:
#         return num*factorial(num-1)
# x=factorial(num)
# print(x)
# Print first n Fibonacci numbers

# Count frequency of each character in a string
# name="pretty"
# freq={}
# for i in name:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)
# 🟡 LEVEL 2 — Lists, Tuples, Dictionaries

# Remove duplicates from a list without using set
# l=[1,2,3,3,1,4,5]
# d=set()
# for i in l:
#     if i not in d:
#         d.add(i)
# print(d)
        
# Find the second largest number in a list

# Merge two lists and sort without using sort()

# Find common elements between two lists

# Convert a list into a dictionary

# ["a", "b", "c"] → { "a": 1, "b": 2, "c": 3 }


# Count frequency of elements in a list using dictionary

# Find key with maximum value in a dictionary

# Reverse a list in place

# Check if two lists are anagrams

# Sort a dictionary by values

# 🟠 LEVEL 3 — Strings (Very common in interviews)

# Find the first non-repeating character in a string

# Check whether two strings are anagrams

# Find the longest word in a sentence

# Remove all spaces from a string

# Replace duplicate characters with _

# Count number of words in a sentence

# Convert "hello world" → "World Hello"

# Find all substrings of a string

# Check if string contains only digits

# Find repeated characters in a string

# 🔵 LEVEL 4 — Functions & Logic

# Write a function that returns multiple values

# Difference between return and print (explain with example)

# Write a function to check Armstrong number

# Write a recursive function for factorial

# Write a function to flatten a nested list

# [1, [2, [3, 4]]] → [1, 2, 3, 4]


# Pass a function as an argument

# Use *args and **kwargs with example

# Explain local vs global variable with code

# Lambda function to find square of numbers

# Map, Filter, Reduce – simple use cases

# 🔴 LEVEL 5 — OOP (Very important for interviews)

# Create a Student class with name and marks

# Use __init__ method — explain why it is used

# Difference between class variable and instance variable

# Demonstrate inheritance with example

# Method overriding example

# What is self? Explain with code

# Encapsulation example

# Create a class with private variable

# Use __str__ method

# Real-world OOP example (Bank / Employee)

# ⚡ BONUS — Common Interview Logic

# Find missing number in a list

# Find pair of numbers with given sum

# Check if list is sorted

# Rotate list by k positions

# Count number of even and odd numbers

# Find duplicates in a list

# Longest consecutive sequence

# Find intersection of two lists

# Implement simple stack using list

# Implement simple queue using list