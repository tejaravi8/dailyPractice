# Check if number is palindrome

# a=12345
# reverse=""
# for i in str(a):
#     reverse=i+reverse
# print(reverse)

# a=12345
# reverse=""
# for i in (str(a)):
#     reverse=i+reverse
# print(reverse)
# a=a = [10, 5, 20, 8, 15] #[10,5,20,8]
# first=second=-float("inf")
# for i in a:
#     if i>first:
#         second=first
#         first=i
#     elif i < first and i > second:
#         second=i
# print(second)


# abc=[1, 2, 2, 3, 4, 4]
# output=[]
# for i in abc:
#     if i not in output:
#         output.append(i)
# print(output)

# 3. First Non-Repeating Character
# abc="aabbcde"
# non={}
# c=0
# for i in abc:
#     if i not in non:
#         non[i]=1
#     else:
#         non[i]+=1
# for i in non:
#     if non[i]==1 and c<1:
#         print(i)
#         c+=1
#         # break

# abc="hello world".split()
# word=""
# rev=""
# for i in abc:
#     word+=i[::-1]
#     rev=rev+word+" "
#     word=""
# print(rev)

# input=[1, 2, 2, 3]
# qbc={}
# for i in input:
#     qbc[i]=qbc.get(i,0)+1
# print(qbc)
# input= [0,1,0,3,12]
# # Output: [1,3,12,0,0]
# q=[]
# a=[]
# for i in input:
#     if i !=0:
#         q.append(i)
#     else:
#         a.append(i)
# array=q+a
# print(array)

# input="MAdam"
# abc=input.lower()
# rev=""
# for i in abc:
#     rev=i+rev
# print(rev==abc)

# Input=[1,2,4,5]

# for i in range(1,len(Input)):
#     if Input[i]-Input[i-1]==2:
#         print(Input[i]-1)
        
# Input = [-2,1,-3,4,-1,2,1,-5,4]

# max_sum=Input[0]
# current_sum=Input[0]

# for i in range(1,len(Input)):
#     current_sum=max(Input[i],current_sum+Input[i])
#     max_sum=max(current_sum,max_sum)
# print(max_sum)