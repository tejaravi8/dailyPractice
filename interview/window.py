# arr = [2,1,5,1,3,2]
# k = 3
# max_sum=0
# while len(arr)>=k:
#     window_sum=0
#     for i in range(k):
#         window_sum+=arr[i]
#     if window_sum>max_sum:
#         max_sum=window_sum
#     arr.pop(0)
# print(max_sum)
    
# window=0
# max_sum=0

# for i in range(k):
#     window+=arr[i]
# max_sum=window
# for i in range(k,len(arr)):
#     window+=arr[i]-arr[i-k]
#     max_sum=max(max_sum,window)

# print(max_sum)
# s1 = "abcd"
# s2 = "dcba"
# rotation=True
# s1=set(s1)
# for i in s2:
#     if i not in s1:
#         rotation=False
#         break
# print(rotation)
# for i in s1:
#     if i not in s2:
#         rotation=False
#         break
# print(rotation)

# 2️⃣ First Negative Number in Every Window of Size K
# arr = [12,-1,-7,8,-15,30,16,28]
# k = 3

# neg=[]
# for i in range(k)

from datetime import datetime
date=datetime.now().strftime("%d-%m-%y %H:%M:%S")

import json

with open("expense.json","r") as file:
    data=json.load(file)
    for i in data:
        
        march_dates = [d.split('-')[1] for d in i["date"] if d.split('-')[1] == '03']
        print(march_dates)