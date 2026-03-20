
# def decorator(func): # a function which modifies the behaviour of another function,without changing its source code.
#     def wrapper():                 
#         print("bojanaluuu")
#         func()
#         print("byeee")
#     return wrapper

# # @decorator  # ==>  marriage = decorator(marriage)
# def marriage():
#     print("happy married life Sai_sailu")

# # marriage()    

# marriage=decorator(marriage)
# # marriage()


# d={"a":1,
#     "b":2}


# for i,j in d.items():
    
# def simple_generator():
    
#     yield "First"
#     yield "Second"
#     yield "Third"
#     print("fghj")

# # Create a generator object
# gen = simple_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))   # stop iteration


# class school:
    
    # def __init__(self,balance):
#         self.__balance=balance
#         self.name="pablo"
    
#     def pablo(self):
#         return self.__balance
    
#     def teja(self):
#         self.bala="teja"
    
# abc=school(5000)
# abc.teja()
# print(abc.bala)

# # print(abc.getter())


# shallow 

# from copy import deepcopy    # different reference
# a=[1,2,3,[9,5]]
# # b=a

# b=deepcopy(a)

# print(id(a),id(b))
# b[3][0]=7

# print(a,b)

# iteration

# print("Hello")
