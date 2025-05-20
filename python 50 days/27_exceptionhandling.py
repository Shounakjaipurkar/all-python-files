#Exception handling in python 
#Exception handling is the process of responding the unwanted and unexpected events in the program during the execution.
#Exception handling deals with the events like this to avoid the program or system crash.
#and without this process exceptions would disrupt the normal flow of the program.

#Python has a built-in exception handling mechanism that allows you to handle the exceptions that are raised during the program execution
#when these exceptions occurs the python interpretour stop the current process and passes it to the calling fucntion .
#until its handled, if not handled the program will crash.


#Python try...except block
#this is used for handling the error in the python
#try block runs when there is no error in the program
#but try block cathes the error in the program then the except block is executed

#Syntax:

a=input("Enter a number: ")
print(f"Multiplicatin table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{a}X{i} =",int(a)*int(i))
except:
    print("invalid input")
print("Out of loop")
print("anything")
#if you enterd the string in the input line no 24 will be executed and the program will not crash.
#insted of crashing the program will print the invalid input and out of loop.
#if you write after anyting after "out of loop" then it will execute"



