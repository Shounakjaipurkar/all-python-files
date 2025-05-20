#dictionary methods
#update()
#The update() method updates the value of the key provided to it if the item already exists in the dictionary, 
#it creates a new key-value pair.
info={"name":"shounak","age":19}
info2={"name":"krishna","age":23,"position":"king","rollno":23}
 
info.update({"name":"jaipurkar"})
print(info)


#clear method removes all the items in the dictionary
info.clear()
print(info) #output:{}

# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.
info2.pop("age")
print(info2)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.
info2.popitem()
print(info2)

# del:
# we can also use the del keyword to remove a dictionary item.
#Note:If key is not provided, then the del keyword will delete the dictionary entirely.

#with keyword
info3 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info3['age']
print(info3)
#Without keyword
# del info3
# print(info3) # if you run this it will generate an error NameError: name 'info3' is not defined
