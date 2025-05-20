#strings mathods have diffrent functions that can be used to manipulate strings
# Remember that strings are immutable in python
#some of the methods are:

print("--------------------------------------------------")
name="shounak, jaipurkar, shounak"
print(name.upper()) #will convert the string into uppercase
print(name.lower()) #will convert the string into lowercase
print(name.replace("shounak","Krishna")) #will replace the first argument with the second argument
print(name.split(" "))
blog="i am a student of computer scieCce engineeRing"
print(blog.capitalize())

print("----------------------------------------------")
# center in the string 
cen="shounak"
print(len(cen))
print((cen.center(50))) #will center the string in the given width
print(len(cen.center(50)))

print("----------------------------------------------")
# for counting 
print(name.count("shounak"))

print("----------------------------------------------")
#for finding string end with what 
print(name.endswith("shounak")) #will return false as the string does not end with shounak

#we can also use the startswith method
print(name.startswith("shounak")) #will return true as the string starts with shounak



print("----------------------------------------------")

#find method
myname="name is shounak jaipurkar studying in the 2nd year he is the honnest man in the world" 
print(myname.find ("shounak")) #will return the index of the first occurance of the string
#for index finding
print(myname.index("shounak")) #will return the index of the first occurance of the string

print("----------------------------------------------")
#printable method
yourname=" my name is shounak \n"
print(yourname.isprintable()) #will return true if all the characters are printable it is printing false cause \n is not printable

print("----------------------------------------------")
# for printing tille
print(yourname.title())