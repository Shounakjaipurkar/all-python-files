# Python Functions
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# Built-in functions
# User-defined functions
# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# Syntax:
# def function_name(parameters):
#   pass
#   # Code and Statements
# Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
# Any parameters and arguments should be placed within the parentheses.
# Rules to naming function are similar to that of naming variables.
# Any statements and other code within the function should be indented.
# Calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)

'''
NOTE:
the return keyword is used within a function to send a value back to wherever the function was called. 
Think of it as a way for a function to "output" a result. Let me break it down:
- When a function is executed, the code inside it runs.
- The return statement allows the function to send a value back to the caller, 
which you can then use in the rest of your program.
'''

#example 
print("----------------------------return------------------------------------")
def add(a,b):
  return a+b,a-b,a*b #fuctino returns these oprations where it is called 

result=add(10,5) 
print(result)

#extra
print(type(result))
result=list(result)
print(type(result))

