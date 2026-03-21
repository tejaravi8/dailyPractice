# try:
#     number=int(input("enter a number: "))
#     result=10/number
# except ZeroDivisionError:
#     print("Zero can't be in denominator")
# except ValueError:
#     print("\nInvalid input, Enter int values only")
# else:
#     print("result :",result)
# finally:
#     print("Exception done")

# a=int("10")
# # print(type(a))
# print(a)

# try:
#     x = int("10")
#     y = 5 / 1
# except:
#     print("Error")
# else:
#     print("Success")
# finally:
#     print("Done")

# else run when no exception occurs, and finally always runs.

# try:
#     y = 10 / 2
#     print("try block entered")
#     x = int("abc")
# except ValueError:
#     print("Value Error occurred")
# except ZeroDivisionError:
#     print("Zero Division Error")
# else:
#     print("Success")
# finally:
#     print("Done")

# try:
#     print(10 / 0)
# except ValueError:
#     print("Handled ValueError")

# age = float(input("Enter age: "))

# if age < 18:
#     raise Exception("You are not eligible")

# print("You can vote")


# age=int(input("enter your age: "))

# if age<18:
#     raise Exception("You can't vote")
# else:
#     print("you can vote")

# try:
#     num = int(input("enter the value here: "))

#     if num < 0:
#         raise ValueError("Negative not allowed")

#     print(10 / num)

# except ValueError as e:
#     print("Error:", e,num)


# num=int(input("Enter Number Here: "))

# try:
#     if num==0:
#         raise ValueError ("Hello")
# except ValueError as e:
#     print("ValueError:",e)
# else:
#     print("No Error Found")
# finally:
#     print("Execution Done")
# try:
#     if num<18:
#         raise Exception("Age Can't be less Than 18")
#     # print("hehee")
# except Exception as e:
#     print("Error: ",e)

# customException

# class MyError(Exception):
#     pass

# num=int(input("eneter number: "))
# try:
#     if num<18:
#         raise MyError("lessthan 18 is not allowed !!")
# except MyError as e:
#     print(e)

# class MyError(Exception):
#     def lock(self):
#         self.name="tejaa"

# num = int(input("enter something: "))

# try:
#     if num != 0:
#         raise MyError("Zero is not allowed")
# except MyError as e:
#         print(e)

# try:
#     print("A")
#     x = int("a")
#     print("B")
# except Exception as e:
#     print(e,"ABC")
# finally:
#     print("D")

# try:
#     print("1")
#     x = 10 / 0
# except Exception:
#     print("2")
# except ZeroDivisionError:
#     print("3")
# finally:
#     print("4")

try:
    print("A")
    x = int("abc")
    print("B")
except ValueError:
    print("C")
finally:
    print("D")
    print(10 / 0)