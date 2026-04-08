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

arr=[1,2,3,4,5]
target=9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==target:
                # print(True)
                print(arr[i],arr[j],arr[k])
# 👉 (1+3+5, 2+3+4)