'''
The os module in Python provides a way to interact with the operating system, 
allowing you to perform tasks like managing files and directories, 
interacting with the file system, and running system commands
'''

import os
#os.mkdir("new") #this will create the file name as "naw" in the python 100 days folder which is the main folder
if (not os.path.exists("new")):
    os.mkdir("new") # if new file is existed already then condition will be false and it will create the file name  as new


for i in range(1,101): 
    #os.mkdir(f"new/day{i}")# this will create the i no of files name as day{i} in the path new/daty , this folder is already been created so i commented it
    os.mkdir(f"new/day1/tuto{i}") # this cmd will create the i no of files name as tuto{i} inside the day1 

