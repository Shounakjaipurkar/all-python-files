# this is the module which is used to tell you if __name__=="__main__" the 34th lecture 
#in this we are creating one function name as welcome and calling it

def welcome():
    print("hey there welcome to 100 days of code by code with harry thankyou for watching!!!")
    print(__name__) 
if __name__=="__main__":  
   welcome()# this line tell you that"ager main tujhe yahi se run karu to tu welcome ko execute kr 
  #aur to agar main.py se run ho raha hai to welcome function ko execute mat kr nahi to mar khayega bsdk

'''
1) The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is 
being run directly or being imported as a module into another script.'

2)In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. 
When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported 
as a module into another script, the __name__ variable is set to the name of the module.

3)Why is it useful?
This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, 
without running the code in the original script. 

4)Is it a necessity?
It's important to note that the if __name__ == "__main__" idiom is not required to run a Python script. 
You can still run a script without it by simply calling the functions or running the code you want to execute directly. 
However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly
 from code that should be imported and used as a module.

In summary, the if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script 
is being run directly or being imported as a module into another script. It allows you to reuse code from a script by 
importing it as a module into another script, without running the code in the original script.

'''