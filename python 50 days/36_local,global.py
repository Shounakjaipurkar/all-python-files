#local variable:A variable that  is declared inside the function is called as the local variable
#eg

def cal():
    a=5 # now these 2 variable are the local variable 
    b=5
    print("the addition of a and b is",a+b) #this is inside the function and also we are calling the variable inside 
#the fucntion so it is called as the local variable and it will work 
cal()
# but if i call the variable a and b outside of the function cal :
'''print(a+b)''' # now if you run this code then it will throw an error 
#python will not able to find a,b variable as they are inside the function and we are calling the 


# Now global variable: tthe variable which is declared outside the function , the name it self says global
a=10 # this variable is declared outside the glo funtion 
def glo():
    print(f"2X{a}={2*a}") #as a is the global variable python is able to find what is the value of a 
    # it will work fine!
glo()


#The global keyword
x = 10 # global variable
def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable
my_function()
print(x) # prints 5
#print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

'''In this example, we used the global keyword to declare that we want to modify the global variable x from within the function. 
As a result, the value of x is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, 
as it can lead to unexpected behavior and make your code harder to debug.

I hope this tutorial has helped clarify the differences between local and global variables and how to use the global keyword
in Python'''