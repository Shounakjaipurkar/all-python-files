s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) #this union method will print the union of s1 and s2
s1.update(s2) #this update method will update the s1 adding the values of s2
print(s1)
print(s1,s2)
print("----------------------------------------------")
#intersection
print(s1.intersection(s2)) #it will print the intersection of set s1 and s2 



# # Joining Sets
# # Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

# # I. union() and update():
# # The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

# # Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)
# # Output:
# # {'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}


# # Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)
# print(cities)
# # # Output:
# # {'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}


# # II. intersection and intersection_update():
# # The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

# # Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)
# # Output:
# # {'Madrid', 'Tokyo'}


# # Example :
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)
# Output:
# {'Tokyo', 'Madrid'}


# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 
# The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
# Output:
# {'Seoul', 'Kabul', 'Berlin', 'Delhi'}

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)
# Output:
# {'Kabul', 'Delhi', 'Berlin', 'Seoul'}

# IV. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)
# Output:
# {'Tokyo', 'Madrid', 'Berlin'}

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))
# Output:
# {'Tokyo', 'Berlin', 'Madrid'}

