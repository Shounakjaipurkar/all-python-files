i=0
while True:
    print(i)
    i=i+1
    if i%100==0:
        break
print("done with the loop")
# How to emulate do while loop in python?
#--->
# To create a do while loop in Python, you need to modify the while loop a 
# bit in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to use an 
# infinite while loop with a break statement wrapped in an if statement that 
# checks a given condition and breaks the iteration if that condition becomes true:
 
