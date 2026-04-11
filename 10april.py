# arr=[1,2,3,4,2,3,1]
# duplicates=[]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j] and arr[j] not in duplicates:
#             duplicates.append(arr[j])
# print(duplicates)

# arr=[1,5,3,4,2]
# k=2
# count=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if abs(arr[i]-arr[j])==k:
#             count+=1
# print(count)

# a=[1,2,3,4,5,6,7]
# i=0
# l=len(a)-1
# while i<int((len(a)/2)):
#     a[i],a[l]=a[l],a[i]
#     i+=1
#     l-=1
# print(a)

# Hashing
# we using hashing to avoid nested loops

# a=[1,2,3,4,2,1]
# seen=set()
# dup=[]
# for i in a:
#     if i not in seen:
#         seen.add(i)
#     else:
#         dup.append(i)
# print(dup)

arr = [2,11,15,7] # 0
# s=set()
# target=9
# for i in arr:
#     s.add(i)
#     if target-i in s:
#         print(target-i,i)

target = 9
t={}
for i in range(len(arr)):
    diff=target-arr[i]  # 2
    if diff in t: 
        print(t[diff],i)
    else:
        t[arr[i]]=i
print(t)

# ar=[1,2,3,2,4,1]
# s=set()
# dup=[]
# for i in ar:
#     if i not in s:
#         s.add(i)
#     else:
#         dup.append(i)
    
# print(dup)

# a=[1,2,2,3,1,4]
# freq={}
# for i in a:
#     freq[i]=freq.get(i,0)+1
# for i in freq:
#     if freq[i]==1:
#         print(i)
        # break
    
# s=set()
# duplicates=[]
# for i in a:
#     if i not in s:
#         s.add(i)
#     else:
#         duplicates.append(i)

# for i in s:
#     if i not in duplicates:
#         print(i)
#         break

