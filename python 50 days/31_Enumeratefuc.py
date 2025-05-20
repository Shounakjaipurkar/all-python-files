'''The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and 
get the index and value of each element in the sequence at the same time. 
Here's a basic example of how it works:'''


mark=[12,23,24,100,89,35,90,69]
# index=0
# for marks in mark:
#     print(marks)
#     if index==3:
#         print("best student in the class!!")
#     index=index+1


    
# for index,marks in enumerate(mark):
#     print(marks)
#     if index==3 or index==4:
#         print("best student in the class: ")
# e.g 2

fruits=['apple','mango','orange','karela']
for index,fruit in enumerate(fruits): 
    
    if index==3:
        print(f"this is {index}.{fruit} and it is not tasty.")
    else:
        print(f"this is {index}.{fruit} and it is tasty.")


#start with in the enumator:
fruits=['apple','mango','orange','karela']
for index,fruit in enumerate(fruits,start=1):  
    ''' this "start" because of this the index which is incrementing 
    #by one and also it is starting from zero now it will start from 1 
    # as we added the start in the enumerator'''
    
    if index==3:
        print(f"this is {index}.{fruit} and it is not tasty.")
    else:
        print(f"this is {index}.{fruit} and it is tasty.")
    

#loop over the tuple and print the index and value.
colors=["red","green","blue"]
for c,color in enumerate(colors):
    print(c,color)
print("--------------------------------------------------------------------------------")
words="hello"
for t,word in enumerate(words):
    print(t,word)


    
        
