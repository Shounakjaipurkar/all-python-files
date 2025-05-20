# format method
letter="hey my name is {} and i am {} years old"
name="shounak"
age="19"
print(letter.format(name,age))
#this will print 
# hey my name is shounak and i am 19 years old




#fstrigs:
print(f"hey my names is {name} and i am {age} years old")
#for 2 decimal places we use this:
price=49.09999

txt=(f"For only {price:.2f} dollors!")
print(txt)
#if you want to show the culry bracket then use double curly bracket:
print(f"hey my names is {{name}} and i am {{age}} years old")

