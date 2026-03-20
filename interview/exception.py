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

try:
    num = int(input("enter the value here: "))

    if num < 0:
        raise ValueError("Negative not allowed")

    print(10 / num)

except ValueError as e:
    print("Error:", e,num)