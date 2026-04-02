# prime check

# num=int(input("enter the number: "))
# count=1
# for i in range(2,num):
#     if num%i==0:
#         count+=1

# if count==1:print(True)
# else:print(False)

# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break
#     else:
#         is_prime=True
# print(is_prime)

# def check_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# def loop_prime(n):
#     for i in n:
#         if check_prime(i):
            

# x=loop_prime([1,2,3,4,5])

# a=[1,2,3,4,5,7,8]
# for i in a:
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print("prime",i)

a=11
b=11
c=12


# if a>=b and a>=c: #a==max(a,b,c):
#     print("a is bigger")
# elif b>=a and b>=c:
#     print("b is biggest")
# else:
#     print("c is biggest")

# if a==max(a,b,c):
#     print('a')
# elif b==max(a,b,c):
#     print("b")
# else:
#     print("c")

# a=0
# b=1
# n=int(input("Enter the n terms: "))
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

x=15
y=18
# freq={}
# for i in a:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# def gcd(a,b):
#     while b:
#         a , b = b , a % b
#     return a

# zxc=gcd(x,y)
# print(zxc)

# set1
# name="hello"
# output=""  # h -> eh -> leh -> lleh -> olleh
# for i in name:
#     output=i+output   
# print(output)
# name="madam"
# rev=""
# if name==name[::-1]:
#     print(True)
# else:
#     print(False)

# nums=[3,5,2,9]
# first=second=-float("inf")
# for i in nums:
#     if i>first:
#         second=first
#         first=i
#     elif i<first and i>second:
#         second=i
# print(first)
# print(second)

# def check_prime(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True

# a,b=0,1
# for i in range(20):
#     x=check_prime(a)
#     if x:
#         print(a)
#     a,b=b,b+a

# name="hello"
# count=0
# for i in name:
#     if i in "aeiou":
#         count+=1
# print(count)

# name="a b c"
# ad=""
# for i in name:
#     if i!=" ":
#         ad+=i
# print(ad)
# # ad=""
# # for i in name:
# #     ad+=i
# # print(ad)

# patterns
# for i in range(5):
#     for j in range(i):
#         print("* ",end="")
#     print()
# for i in range(1,5):
#     print("* "*i)
# for i in range(1,6):
#     num=1
#     for j in range(i):
#         print(num,end="")
#         num+=1
#     print()

# a,b=6,12
# a1,a2=a,b

# while a2:
#     a1,a2=a2,a1%a2
#     gc=a1

# lcm=(a*b)/gc
# print(lcm)
# a=[1,2,3,5]
# s=0
# for i in a:
#     s+=i
# print(s)

# a=[1,2,3,4]
# k=2
# k=k%len(a)
# print(a[-k:]+a[:-k])
# n="aab"
# freq={}
# for i in n:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# num=153
# temp=num
# count=int(len(str(num)))
# output=0
# while temp>0:
#     output+=(temp%10)**count
#     temp//=10
# if output==num:
#     print(True)
# else:
#     print(False)
# num=123
# output=0
# while num>0:
#     output+=num%10
#     num//=10
# print(output)
a="abcde"
b="cdeab"

if ( len(a) == len(b) and b in a+a ):
    print(True)
else:
    print(False)

# nums=[1,2,4,5]
# n=len(nums)+1
# left=(n*(n+1))/2
# s=sum(nums)
# print(int(left-s))