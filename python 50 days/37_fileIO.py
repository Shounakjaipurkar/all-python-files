#if the path is in somewhere else not in the same derectory
#copy the path of the file first using right click and then copy as a path
f=open(r"C:\Users\shoun\OneDrive\Desktop\decfile.txt.txt",'r') #r is for windows oprating system
data=f.read()
f.close()
print(data)

#why we close the file after opening it:
#because if we do not close the file, it will not be saved and the data will be lost.
#and also it will not be able to open the file again.

#why we can not open the file again
#because the file is already opened and it is not closed yet.
#so we have to close the file first and then open it again.



f=open('myfile.txt','r')
text=f.read()
print(text) #This will print the text inside the myfile.txt
f.close()


#Now focus here:
f=open('myfile.txt') #here we are not writing 'r' after myfile.txt 
text=f.read()
print(text) #This will print the text inside the myfile.txt
f.close()

#although we are not typing 'r' after the myfile.txt this program will run succesfully 
# as the 'r' is default in it if we did't write it  will read




# j=open('myfile2.txt','r')
# text2=j.write()
#this will give us an the error because in first line(6) we are tellin it to read and then again we are tellin it to write(7)
#so because of it this will throw an error 

#write

# Note: If you didn't create the file and then you called the write function, the file will be created automatically.

k=open('myfile2.txt','w')
k.write('Hi shounak jaipurkar!!')
k.close()  # Always remember to close the file 
#after executing the code chnech the myfile2.txt the text will be added automatically that is 'Hi shounak jaipurkar'


#append
#append also create the file if it is not present

g=open('mytext2.txt','a') # this is append
g.write('Hi !!, ') # after runnig the code chech mytext2.txt the hi text will be appended to the end of it 

# Each time when you run the code the 'Hi' will be added at the end of the text 
# Rem-Append mean inceasing from end 


#with statement in python

with open('mytext2.txt','a') as k:
    k.write("Hey i am adding this using with statement") #This text will be added at the end of the file
    #By with statement we dont have to close the file




