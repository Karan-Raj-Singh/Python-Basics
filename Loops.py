# If, Elif and Else function in python
"Age cycle of a  person"
age=input("enter your age in integer:" )
age=int(age)
if age <=3:
    print (" you are a baby")
elif age >=4 and age <=12:
    print("You are a child")
elif age >=13 and age<=19:
    print("You are a teenager")
elif age >=20 and age<=34:
    print("You are a young adult")
elif age>= 35 and age<=64:
    print("You are middle aged")
else:
    print("You are a senior citizen")

# Presenting while loop
# making a  mountain pattern in the while loop
x=0
while x<=15:
    print(x*"**")
    x+=1
x=15
while x>=0:
    print(x*"**")
    x -=1

#for loop in
for i in range(20):
    print("best")

# Using if and while loop
# Name guessing game
name="karan"
while True:
    x = input("Enter your name: ")
    if x==name:
        print("perfect")
        break
# we use the break function to immediately break the loop
c=0

