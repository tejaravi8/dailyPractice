
# Expenses={}
# Expenses["food"]=20
# Expenses["vegetables"]=30
# Expenses["vegetable"]=152

# print(Expenses)
# s=0
# for i in Expenses:
#     s+=Expenses[i]
# print(s)
import json

class ZeroError(Exception):
    pass
class NegativeError(Exception):
    pass
class myerror(Exception):
    pass

def AddExpense():
    try:
        amount=int(input("\nEnter Amount of Expense: "))
        category=input("Enter the Category of Expense: ")
        if amount==0:
            raise ZeroError("\nExpense can't be Zero '0' ")
        elif amount<0:
            raise NegativeError("\nExpense can't be in Negeative")
    except ValueError:
                print("\nEnter Integer values only")
    except ZeroError as z:
        print(z)
    except NegativeError as N:
        print(N)
    else:
        return {"amount":amount,"category":category}
    finally:
        print("\nAdd Expense Function Worked")

def ViewTotal():
    total=0
    try:
        with open("expense.json","r") as file:
            data=json.load(file)
            for i in data:
                total+=i['amount']
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
            raise myerror("\n!! Choose Mentioned options only !!")
        
        if option==1:
            abc=AddExpense()
            
            if abc is not None:
                with open("expense.json","r") as file:
                    data=json.load(file)
                
                with open("expense.json","w") as file:
                    data.append(abc)
                    json.dump(data,file,indent=4)
                
        elif option ==2:
            try:
                with open("expense.json","r") as file:
                    data=json.load(file)
                    print("\n---------Expenses----------")
                    for i in data:
                        print(f"{i["category"]} - {i["amount"]}")
                    print("---------------------------")
            except FileNotFoundError:
                print("\nNo Expenses Found")
            
        elif option ==3:
            total=ViewTotal()
            print("\nTotal Expenses : $",total)
        elif option==0:
            print("\nThanks for Using Expense Tracker")
            break
    except ValueError:
        print("\n!! Enter valid integer values only !!")
    except myerror as n:
        print(n)
    