# Lets start with the basic coding
# use the print function while executing the function to see the output in the command prompt
print ("Hello World")
# Basic Maths and variables and strings
x=1+1
print(x)
x=3/2
print(x)
x=5//2
print(x)
x=3*2
print(x)
# there are 3 types of data in the python
# Strings, Integers, Float
# Variable when you assign any of the data type to something
x= "a"
print(x)
a=1
b=1.2
print(a)
print(b)
# assigning multiple variables values at once
x,y,z= 1,2,3
print (x)
print (y)
print(z)
a=b=c=d=10
print (a)
print(b)
print(c)
print(d)
a= 10
b= "Python"
c= 10.354
print(type(a))
print(type(b))
print(type(c))
# Set it is used to store multiple items in single variable
s= set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
s.remove(3)
print(s)
# List is a store things collected together
x=["Apple","Mango","Grapes",12,"12"]
# we can slice through the list
print(x[0:5:2])
# slicing can also be started from backwards
print(x[-1:-2:-1])
# Now some operations on the list that can be done are sort, reverse, isnum,upper, lower, find, endswith, insert, pop
x=["Apple","Orange","Banana","Mango"]
x.sort()
x.append("Grapes")
x.insert(1,"Watermelon")
# Tuple is a fixed form of list
a= (1,2,3,4)
# Dictionery for storing values and keys in the
a= {"Name":"Karan", "Age":"24","Location":"Dublin"}
print(a)
# we can also add a dictionery in a dictionery
b=a.copy()
print(b)
b["Country"]="Ireland"
print(b)
