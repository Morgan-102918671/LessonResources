#Lesson 3 May 4 Period 1 (I was originally going to teach 2 periods but ended up teaching 1)

#Please note that this code was orginally shown on replit.com and had a lot of whitespace to make sure that the students did not see all of the code

a = 3.14
b = 2.72
c = 0.58
if a>b:
  print("a is greater than b")
else:
  print("b is greater than a")

if b == 2.72:
    print("b equals 2.72")
else:
    print("b does not equal 2.72")

if c >= 10:
    print ("yes")
else:
    print("no")

#calculate area of rectangle
length = int(input("Enter a number the length: "))
width = int(input("Enter a number the width: "))
print ("the area of the rectangle is: ", length*width, " square units")

#calculating the area of a circle
radius = int(input("Enter the value of the radius: "))
print ("the area of the circle is: ", 3.14*radius*radius)

#IF Statements
number = int(input("What is the number? "))
#The % function gives the remainder after division
if number % 2 == 0:
    print(number,'is even.')
else:
    print(number,'is odd.')

#This was a task I assigned but ended up not showing the class
#Option 1
#Ask the user if they want to + or -
AorS = input("Do you want to use + or -? ")
#Ask the user for number 1
number1 = int(input("What is number 1? "))
#Ask the user for number 2
number2 = int(input("What is number 2? "))
#Calculate
#Print calculation
if AorS=="+":
    print("The calculation is: ", number1+number2)
else:
    print("The calculation is ", number1-number2)

#Option 2
#Ask the user if they want to + or -
AorS2 = input("Do you want to use + or -? ")
#Ask for number 1
number1v2 = int(input("What is number 1? "))
number2v2 = int(input("What is number 2? "))
#Calculate
if AorS2 == "+":
    addition = number1v2+number2v2
else:
    subtraction = number1v2-number2v2
#Print calculation
if AorS2 == "+":
    print("The calculation is", addition)
else:
    print("The calculation is ", subtraction)

#I did not end up using this code
#elif
var = input("1, 2 or 3? ")
if var=="1":
    print("You have selected option 1")
elif var=="2":
    print("You have selected option 2")
else:
    print("You have selected option 3")

#I did not end up using this code
#This is an elaboration on the calculator task
MDSA = input("Do you want to use *, /, - or +? ")
number3 = int(input("What is the first number? "))
number4 = int(input("What is the second number? "))

if MDSA=="+":
    print("The calculation is ", number3+number4)
elif MDSA=="-":
    print("The calculation is ", number3-number4)
elif MDSA=="*":
    print("The calculation is ", number3*number4)
else:
    print("The calculation is ", number3/number4)