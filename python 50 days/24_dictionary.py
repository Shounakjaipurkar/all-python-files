#python dictionary
#dictionary are ordered collection of data items,Store multiple items in a single variable,
# dictinary items are key value pair
#that are seprated by comma and enclosed in curly braces {}
#dictionary is mutable
#dictionary is unordered

info={
    "name":"shounak",
    "age":18,
    "city":"nagpur",
    "eligible":"Yes!!"
}
print(info) # this will print the whole dictionary
print("my name is",info["name"])# this is for accessing the value of the key
print("my age is",info["age"])
print("my city is",info["city"])
#.get is used to access the value of the key and if the key is not present then it will return None instead of giving an error

print("is he eligible for voting",info.get("eligible") ) # If we used .get then it will return None if the key is not present
# print(info.get("name2") )# this will print None because the key is not present
# print(info["name2"]) # this will give an error because the key is not present


#for accesing the keys 
print(info.keys())
#Using for loop we can itrate over the keys
for key in info.keys():
    print(info[key])

#for accesing the values
print(info.values())


#for key and value
print(info.items())
for key,value in info.items():
    print(f"thie key is {key} and the value is {value}")