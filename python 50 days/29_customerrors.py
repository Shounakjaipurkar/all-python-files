#custom errors in python
#in python we can raise custom errors by using raise keyword in python.

i=input("Enter here: ")
p=i
if i=="Quit":
    print("okay")
 
elif int(p)<5 or int(p)>9:
    raise ValueError

# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:    #focus on the if not here 
#     raise ValueError("Not a valid salary")