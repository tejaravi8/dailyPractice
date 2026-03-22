# # file=open("first.txt","r")
# # # file.write("hii")
# # # file.write("hello sir")
# # print(file.read())
# # # print(r)
# # file.close

# # with open("data.txt", "a+") as f:
# #     print(f.read())
# #     f.write("Added\n")
    
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

# import csv

# with open("expense.csv","w") as file:
#     a=csv.writer(file)
#     a.writerow(["name","age","phone"])
#     a.writerow(["teja",21,9391254093])



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

import json
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

import json
data={ "name": "Raviteja","age": 21,"phone": 9391254093}

with open("expense.json","r") as file:
    reader=json.load(file)
    print(reader)