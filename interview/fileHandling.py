# file handling : 

# file handling is the process by which a computer programm that 
# creates, opens,reads ,writes and manage file stored on a desk


# methods: 4types
# 1. write - w 2. read - r 3. create - x 4. append - a 

# 5. r+ / w+ / a+ ( optional)

# file = open("ganesh.txt","w")
# file.write("ganesh")
# file.close()
# data=["pablo","teja","bro","charan","sailu"]
# with open("sailu.txt","w") as file:
#     for i in data:
#         file.write(i+"\n")
        # pointer
# writelines, write
# data=["pablo","teja","bro","charan","sailu"]
# with open("sailu.txt","r") as file:
#     v=read()
#     # read(), readlines - list , readline
#     # v=file.readlines() 
#     # v1=file.readline() 
#     # v2=file.readline() 
#     # v2=file.readline()# we can access through index
#     # print(v)
#     file.write("tejjaa")

# import json

# data=[
#   {
#     "id": 1,
#     "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
#     "price": 109.95,
#     "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
#     "category": "men's clothing",
#     "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
#     "rating": {
#       "rate": 3.9,
#       "count": 120
#     }
#   },
#   {
#     "id": 2,
#     "title": "Mens Casual Premium Slim Fit T-Shirts ",
#     "price": 22.3,
#     "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
#     "category": "men's clothing",
#     "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
#     "rating": {
#       "rate": 4.1,
#       "count": 259
#     }
#   },
#   {
#     "id": 3,
#     "title": "Mens Cotton Jacket",
#     "price": 55.99,
#     "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
#     "category": "men's clothing",
#     "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
#     "rating": {
#       "rate": 4.7,
#       "count": 500
#     }
#   }]
# with open("ganesh.json","w") as file:
#     json.dump(data,file,indent=4)
    # file.write()
    
import csv

    # with open("sailu.txt","w") as file:
    #     file.writelines(v)

# # file.write("hii")
# # file.write("hello sir")
# print(file.read())
# # print(r)
# file.close

# ganesh=open("ganesh.txt","")

# with open("data.txt", "a+") as f:
#     print(f.read())
#     f.write("Added\n")
    
# # print("done")
# # with open("data.txt", "r+") as f:
# #     print(f.read())
# #     f.writelines(["teja\n","chandu","charan","akash","nani","devudu","shiva","sai","kishore","nanna","venkateswara"])

# # with open("data.txt", "r") as f:
# #     for line in f:
# #         print(line.strip())
        
# # with open("data.txt", "r") as f:
# #     print(f.tell())   # 0
# #     print(f.seek())
#     # print(f.read())   # 5
#     # print(f.read(),"readdd")
#     # print(f.read(),"read")
#     # print(f.read(),"read")
#     # for line in f:
#     #     print(line.strip())
    
# with open("test.txt", "w") as f:
#     f.write("ABCDE")

# with open("test.txt", "r") as f:
#     print(f.read(2))
#     print(f.read(2))
#     print(f.tell())

# CSV File Handling
# CSV = Comma Separated Values

import csv

with open("ganesh.csv","r") as file:
    av=csv.reader(file)
    print(list(av))
    # var=csv.writer(file)  #curser
    # var.writerow([1235,"tejaaj"])
    # a.writerow(["name","age","phone"])
    # a.writerow(["teja",21,9391254093])



# with open("expenses.csv", "w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Amount", "Category"])
#     writer.writerow([100, "Food"])
#     writer.writerow([200, "Travel"])

# import csv

# with open("rama.csv","a",newline="") as c:
#     reader=csv.writer(c)
#     reader.writerow([300,"Accessories"])

# with open("rama.csv","a",newline="") as file:
#     Headers=["Amount","Category"]
#     writer=csv.DictWriter(file,fieldnames=Headers)
#     writer.writeheader()
#     writer.writerow({"Amount":1000,"Category":"Electronics"})
    
# with open("rama.csv","r") as file:
#     reader=csv.DictReader(file)
#     for i in reader:
#         print(i["Amount"],i["Category"])

# with open("rama.csv","a",newline="") as file:
#     fields=["Amount","Category"]
#     writer=csv.DictWriter(file,fieldnames=fields)
#     writer.writerow({"Amount":10000,"Category":"Mobiles"})

# with open("rama.csv",'a',newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["Amount","Category"])
#     writer.writerow([129999,"Iphone"])

# json files

# import json
# data={
#     "name":"raviteja",
#     "age":21,
#     "mobile":9391254093
# }

# with open("expense.json","w") as file:
#     json.dump(data,file)
# data={ "name": "raviteja", "age": 21, "mobile": 9391254093 }
# with open("js.json","w") as f:
# ddd=json.dumps(data,indent=4)
# print(ddd)

# import json

# data = {"name": "Alice", "age": 30}
# json_string = json.dumps(data, indent=4)
# print(json_string)


# # with open("expense.json","r") as file:
# #     a=json.loads(data)
# #     print(a)

# import json

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# # Convert Python dictionary to a compact JSON string
# json_string_compact = json.load(data,data)
# print("Compact JSON String:", json_string_compact)

# Convert to a human-readable, pretty-printed JSON string
# json_string_pretty = json.dumps(data, indent=4)
# print("Pretty JSON String:")
# print(json_string_pretty)

# import csv
# with open("raviteja.csv","r") as file:
#     reader=csv.reader(file)
#     for i in reader:
#         print(i)

# import json
# data={ "name": "Raviteja","age": 21,"phone": 9391254093}

# with open("expense.json","r") as file:
#     reader=json.load(file)
#     print(reader)