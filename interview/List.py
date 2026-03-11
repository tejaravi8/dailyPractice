# 1️⃣ Find Second Largest Element

# nums=[10,10,10]
# first=second=-float("inf")
# for i in nums:
#     if i>first:
#         second=first
#         first=i
#     elif i>second and i<=first:
#         second=i
# print(second)

# # 2️⃣ Count Frequency of Each Element
# nums=[1, 2, 2, 3, 1, 4, 2]
# freq={}
# for i in nums:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# from collections import Counter
# print(Counter(nums))
# freq={}
# for i in nums:
#     freq[3]=freq.get(3,0)+1
#     print(freq)
# freq={}
# for i in nums:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

# # 3️⃣ Move All Zeros to End
# nums=[0, 1, 0, 3, 12]
# result1=[]
# result2=[]
# for i in nums:
#     if i!=0:
#         result1.append(i)
#     else:
#         result2.append(i)
# rest=result1+result2
# print(rest)


# nums = [0, 1, 0, 3, 12]

# i=0
# for j in range(len(nums)):
#     if nums[j] ==0:
#         continue
#     nums[i],nums[j]=nums[j],nums[i]
#     i+=1
# print(nums)

# data = {"a": 10, "b": 20}
# print(data.get("n",0))

# nums=[4, 5, 1, 2, 0, 4]
# freq={}
# for i in nums:
#     freq[i]=freq.get(i,0)+1
# for i in freq:
#     if freq.get(i)==1:
#         print(i)
        
# # print(freq)
# # for i in freq:
# #     if freq[i]==1:
# #         print(i)
# #         break

# Two Sum 

# nums = [2, 7, 11, 15]
# target = 9
# look={}
# for i,j in enumerate(nums):
#     val=target-j
#     if val in look:
#         print([look[val],i])
#     look[j]=i

# find missing number

nums=[4, 5, 7]
n=len(nums)+1
expected=n*(n+1)//2
act_sum=sum(nums)
print(expected-act_sum)

# for i in range(1,len(nums)):
#     if nums[i]-nums[i-1]==2:
#         print(nums[i]-1)


# check if array is sorted
# nums=[1, 2, 3, 4]
# n=-float("inf")
# for i in nums:
#     if i>n:
#         n=i
#     else:
#         print(False)
#         break
# print(True)

# 7️⃣ Find Duplicate Number

# nums=[1, 3, 4, 2, 2]
# s=set()
# for i in nums:
#     if i not in s:
#         s.add(i)
#     else:
#         print(i)


# nondup=[]
# for i in nums:
#     if i not in nondup:
#         nondup.append(i)
#     else:
#         print(i)
    
# freq={}
# for i in nums:
#     freq[i]=freq.get(i,0)+1

# for i in freq:
#     if freq[i]>1:
#         print(i)

# # 8️⃣ Rotate Array by K Steps

# arr = [1,2,3,4,5]
# k = 2
# output=arr[-k:]+arr[:k+1]
# print(output)

# 9️⃣ Maximum Subarray Sum (Very Important)

# nums= [-2,1,-3,4,-1,2,1,-5,4]
# current_sum=nums[0]
# max_sum=nums[0]
# for i in range(1,len(nums)):
#     current_sum=max(nums[i],current_sum+nums[i])
#     max_sum=max(max_sum,current_sum)
# print(max_sum)


