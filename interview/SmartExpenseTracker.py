
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
    finally:
        print("Add Expense Function Worked")

def ViewTotal():
    total=0
    try:
        with open("expenses.txt","r") as Expenses:
            for i in Expenses:
                total+=int(i.strip())
    except FileNotFoundError:
        print("No expenses Found")
    return total
            

while True:
    try:
        option=int(input(""" 
1. Add Expense 
2. Show Expense
3. Total Expense
0. Break / Stop

Choose Option ( 1 / 2 / 3 / 0) : """))
        if option<0 or option>3:
            raise NegativeError("\n!! Choose Mentioned options only !!")
        if option==1:
            abc=AddExpense()
            if abc is not None:
                with open("expenses.txt","a") as Expenses:
                    Expenses.write(str(abc)+"\n")
                
        elif option ==2:
            try:
                with open("expenses.txt","r") as Expenses:
                    print("\n---------Expenses----------")
                    for i in Expenses:
                        print(i.strip())
                    print("---------------------------")
            except FileNotFoundError:
                print("No Expenses Found")
            
        elif option ==3:
            total=ViewTotal()
            print("Total Expenses : ",total)
        elif option==0:
            print("Thanks for Using Expense Tracker")
            break
    except ValueError:
        print("\n!! Enter valid integer values only !!")
    except NegativeError as n:
        print(n)
    