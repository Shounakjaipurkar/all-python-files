#this is the code for the simple calculator
while True:
  opration=input("Enter the opration that you want to perform +,-,*,/:")
  if opration!=["+","-","*","/"]:
        print("invalid opraion")
   
  def addtion():
    
       num1=int(input("Enter the first number: "))
       num2=int(input("Enter the seconde number: "))
       print(f"the addtion of {num1} and {num2} is",num1+num2)

  def sub():
       num1=int(input("Enter the first number: "))
       num2=int(input("Enter the seconde number: "))
       print(f"the subtraction of {num1} and {num2} is",num1-num2)
  def mul():
       
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the seconde number: "))
        print(f"the multiplication of {num1} and {num2} is",num1*num2)

  def division():
        
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the seconde number: "))
        if num2==0:
                print("can not divide by zero")
        elif num1==0:
               print("it will be infinite")
        else:
            print(f"the division of {num1} and {num2} is",num1/num2)
  if opration=="+":
        addtion()
  elif opration=="-":
        sub()
  elif opration=="*":
        mul()
  elif opration=="/":
        division()
# else:
#         print("invalid opration") you can use this line of 4th line that is if statement
  reapeat=input("Do you want to repeat again:yes/no: ")
  if reapeat!="yes":
        print("We identified an invalid input so\nThank you for using our calculator ")
        break

       

       
       
       



