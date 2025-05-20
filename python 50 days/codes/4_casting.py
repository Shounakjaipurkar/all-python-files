#cating
c=5
print(type(c))
#it wil print <class 'int'>
c=str(5)
print(type(c))
#it will print <class 'str'>

#type casting :the conversion of one data type into another data type
a="1"
b="2"
print(int(a)+int(b))

#explicit type casting(casting done by the user)

string="15"
number=7
string_number=int(string)
sum=(string_number+number)
print("sum is: ",sum)


#implicit type casting(casting done by the python it self)
c=9.4
b=5
print(c+b)