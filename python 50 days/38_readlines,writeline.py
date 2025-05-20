#readlines() method
#read lines method reads the single line from the file.If we want to read multiple lines then we can use loop.

f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line: #The while loop itrates through the lines if the line is ended then this condition will me true  
        # print(line,type(line)) #remove the comment of this you will only have the type of the line but it will not print the whole line
      break
    print(line)   #cuase here the condition is true 

    


f = open('myfile2.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)

'''writelines() method
The writelines() method in Python writes a sequence of strings to a file. 
The sequence can be any iterable object, such as a list or a tuple.'''

f=open('mytext2.txt','w')
lines=['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()