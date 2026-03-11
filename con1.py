# econd largest element without sorting.

# Input: [4, 1, 7, 3, 9, 7]
# Output: 7
# arr=[4,4]
# first=second=-float("inf")

# for i in arr:
#     if i>first:
#         second=first
#         first=i
#     elif i>second and i!=first:
#         second=i

# if second==-float("inf"):
#     print("No second number")
# else:
#     print(second)

# arr = [2, 3, 10, 6, 4, 8, 1]

# min_val=arr[0]
# max_dif=0

# for i in range(1,len(arr)):
#     for j in range(i):
#         if (arr[i]-arr[j])>max_dif:
#             max_dif= arr[i]-arr[j]

# print(max_dif)
            
# for i in range(1,len(arr)):
#     if arr[i]>min_val:
#         max_dif=max(max_dif,arr[i]-min_val)
#     else:
#         min_val=arr[i]

# print(max_dif)

# arr=[4, 2, -3, 1, 6]
# window=[]
# for i in range(1,len(arr)):
    
    

# a1="listen"
# a2= "silent"

# freq={}
# for i in a1:
#     freq[i]=freq.get(i,0)+1

# for i in freq:
#     if i in a2:
#         freq[i]-=1

# print(freq)
# print(all([freq[i]==0 for i in freq]))

# arr=[1,2,3,4,5]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)

# rev=[]
# for i in arr:
#     rev=[i]+rev
# print(rev)

# for i in range(len(arr)-1,-1,-1):
#     rev.append(arr[i])
# print(rev)

# arr = [1,2,3,4,5]

# last = arr[-]

# for i in range(len(arr)-1, 0, -1):
#     arr[i] = arr[i-1]

# arr[0] = last

# print(arr)

# Input= [16,17,4,3,5,2]

# left=0
# leaders=[]
# for right in range(1,len(Input)):
#     if Input[left]<Input[right]:
#         leaders.append(Input[right])
#     left+=1
# leaders.append(Input[-1])
    
# print(leaders)      
# Output= [17,5,2]

# arr = [1,2,3,4,5,6,7]
# k = 3

# n = len(arr)
# k = k % n

# # Reverse entire array
# left = 0
# right = n - 1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1

# # Reverse first k
# left = 0
# right = k - 1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1

# # Reverse remaining
# left = k
# right = n - 1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1

# print(arr)