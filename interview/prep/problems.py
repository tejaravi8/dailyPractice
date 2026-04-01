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

if a==max(a,b,c):
    print('a')
elif b==max(a,b,c):
    print("b")
else:
    print("c")

            