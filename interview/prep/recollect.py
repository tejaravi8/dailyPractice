# abc=input("eneter something: ").split()
# while True:
#     arr_values=list(input("enter: ").split())
#     print(arr_values)

# abc=list(map(int,input().split()))
# print(abc)

# n = int(input())
# arr = list(map(int, input().split()))
# print("-----------------")
# # print(arr)
# for i in arr:
#     print(type(i),i)
# print("-----------------")

# freq={'banana': 3, 'pple': 2, 'range': 1}

# lowest=min(freq.values())
# high=max(freq.values())

# low=[i for i,j in freq.items() if j==lowest]
# high=[i for i,j in freq.items() if j==high]
# print(min(low),"  ",max(high))
# print(min(freq.keys()))

# students=list(map(int,input("enter: ").split()))

# freq={}
# for i in students:
#     freq[i]=freq.get(i,0)+1

# print(freq)
# max_count=max(freq.values())
# min_count=min(freq.values())

# max_marks=[i for i,j in freq.items() if j==max_count]
# min_marks=[i for i,j in freq.items() if j==min_count]

# print("\nmarks: ",f'{min_marks[0]}  {max_marks[0]}')