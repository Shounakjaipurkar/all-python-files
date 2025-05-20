import random

option=input("Do you want to roll the dice:yes/no")

if option.lower()=="yes":
    while True:
     num=random.randint(1,6)
     print(num)
     repeat=input("Do you want to repeat:yes/no")
     if repeat!="yes":
        print("Thnak you for using diceroll.com :)")
        break 
elif option.lower()=="no":
   print("Thank you")
else:
   print("invalid input")
