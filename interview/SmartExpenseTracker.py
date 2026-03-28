
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
from datetime import datetime
date=datetime.now().strftime("%d-%m-%y %H:%M:%S")
# Errors

class ZeroError(Exception):
    pass
class NegativeError(Exception):
    pass
class myerror(Exception):
    pass

# Load Data
def load_data():
    try:
        with open("expense.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def AddExpense():
    try:
        amount=int(input("\nEnter Amount of Expense: "))
        if amount==0:
            raise ZeroError("\nExpense can't be Zero '0' ")
        elif amount<0:
            raise NegativeError("\nExpense can't be in Negeative")
        category=input("Enter the Category of Expense: ")
    except ValueError:
                print("\nEnter Integer values only")
    except ZeroError as z:
        print(z)
    except NegativeError as N:
        print(N)
    else:
        print("\n Expense Added Successfully")
        return {"amount":amount,"category":category,"date":date}

def ViewTotal():
    total=0
    data=load_data()
    for expense in data:
        total+=expense['amount']
        
    return f"""
-----------------------------
|  Total expenses - {total}  |
-----------------------------
"""

def delete():
    data=load_data()
    category=input("enter your category: ")
    for i in data:
        if i["category"] == category :
            data.remove(i)
    with open("expense.json","w") as file:
        json.dump(data,file,indent=4)

while True:
    try:
        option=int(input(""" 
1. Add Expense 
2. Show Expense
3. Total Expense
4. Search By Category
5. Delete Expense by Category
0. Break / Stop

Choose Option ( 1 / 2 / 3 / 4 / 5 / 0) : """))
        if option<0 or option>5:
            raise myerror("\n!! Choose Mentioned options only !!")
        
        if option==1:
            abc=AddExpense()
            
            if abc is not None:
                data=load_data()
                
                with open("expense.json","w") as file:
                    data.append(abc)
                    json.dump(data,file,indent=4)
                
        elif option ==2:
            data=load_data()
            print("\n---------Expenses----------")
            for i in data:
                print(f"{i["category"]} - {i["amount"]}")
            print("---------------------------")
            
        elif option ==3:
            total=ViewTotal()
            print(total)
        
        elif option==4:
            data=load_data()
            expense=0
        
            category=input("Enter your category to filter: ")
            for i in data:
                if i['category']==category:
                    expense+=i['amount']
            if expense<=0:
                print(f"\n{category} category not found")
            else:
                print(f"\nExpense for the '{category}' is : {expense}")
        elif option==5:
            delete()
        elif option==0:
            print("\nThanks for Using Expense Tracker")
            break
    except ValueError:
        print("\n!! Enter valid integer values only !!")
    except myerror as n:
        print(n)
    