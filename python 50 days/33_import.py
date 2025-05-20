# import math
# print(math.floor(4.3455))
# print(dir(math)) #this will print all the fucntion in the math\
# print("------------------------------------------------------------------------------")
# print(type(math.nan))

'''from shounak import *'''# When you use import * , Python brings in every single function and variable from the other module into your own.
#It's certainly quick and easy, but it can lead to confusion and bugs! This can lead to unexpected behavior in your code + making debugging extra hard.
from shounak import intro,age
intro()
print(f"my age is {age}")

#this is how we can import our own module in another file

