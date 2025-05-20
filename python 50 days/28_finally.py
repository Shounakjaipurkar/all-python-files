# Finally Clause
# The finally code block is also a part of exception handling. 
# When we handle exception using the try and except block, we can include a finally block at the end.
# The finally block is always executed,
# so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.


def num():
    try:
      n=int(input("Enter the number: "))
    except:
       print("invalid input") 
    finally:
      print("This will always execute")
num()


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)


#most doubt of the finally keyword is:
# try:
#   n=int(input("Enter the number: "))
# except:
#   print("invalid input") 

# print("this line will alwayd execute") #this line will always execute without the finally keyword then whats the use of the finally keyword
#the main use of the finally keyword is when you excute this program inside the funtion the this line will not execute 
#so for inside of the fuction we use finally keyword for executing the finally block ,


 


