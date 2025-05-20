# Python Sets
# Sets are unordered collection of data items. 
# They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are unchangeable, meaning you cannot change items of the set once created. '''Sets do not contain duplicate items.'''

info = {"Carla", 19, False, 5.9, 19}# note that 19 is repeated so Sets are unordered collection of data items so 19 will print unorderly in output
#every time it will chnage its position when you run the code
print(info)
#this is how you can accsess the set
for value in info:
    print(value)


harry={}
print(type(harry))
#this is the empty dictionary 

har=set()
print(type(har))
#now this is the empty set
