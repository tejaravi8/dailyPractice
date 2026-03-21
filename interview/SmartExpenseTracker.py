Expenses=[]

# Expenses={}
# Expenses["food"]=20
# Expenses["vegetables"]=30
# Expenses["vegetable"]=152

# print(Expenses)
# s=0
# for i in Expenses:
#     s+=Expenses[i]
# print(s)
class ZeroError(Exception):
    pass
class NegativeError(Exception):
    pass

def AddExpense():
    try:
        amount=int(input("Enter Amount of Expense: "))
        if amount==0:
            raise ZeroError("Expense can't be Zero '0' ")
        elif amount<0:
            raise NegativeError("Expense can't be in Negeative")
    except ValueError:
        print("Enter Integer values only")
    except ZeroError as z:
        print(z)
    except NegativeError as N:
        print(N)
    else:
        return amount

def ViewTotal():
    return sum(Expenses)

while True:
    option=int(input("Choose Option: "))
    if option==1:
        abc=AddExpense()
        if abc!=None:
            Expenses.append(abc)
    elif option ==2:
        print("---------Expenses----------")
        for i in Expenses:
            print(i)
        print("---------------------------")
    elif option ==3:
        abc=ViewTotal()
        print("Total Expenses : ",abc)
    else:
        break