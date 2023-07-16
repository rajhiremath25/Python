# Dictionary is unordered collection of key value pairs enclosed within {}
# Dictionary is mutable

dict1 = {"Apple": 50, "Oranges": 40, "Mangoes": 100}
print(type(dict1))
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1["Banana"] = 10
print(dict1)

dict1["Banana"] = 20
print(dict1)

dict1 = {"frui1": "value1", "fruit2": "value2"}
dict2 = {"frui3": 3 ,"fruit4": "value4"}
dict1.update(dict2)
print(dict1)

dict1.pop("fruit2")
print(dict1)


