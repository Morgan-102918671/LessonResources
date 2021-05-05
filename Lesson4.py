#Lesson 4

#Please note that this code was orginally shown on replit.com and had a lot of whitespace to make sure that the students
#did not see all of the code

#Please note that on replit.com this code is shown in different files so I could different parts of the code separately.
#I have put all the code in one file for convenience

#At start of lesson
import math

#Last lesson
x = int(input("What is the length: "))
y = int(input("What is the width: "))

area = x * y
print(area)

#create a Pythagoras theorem calculator
#c^2=a^2+b^2
#instead of using ^ to square we use **

a = float(input("What is the value of a? "))
b = float(input("What is the value of b? "))
c1 = a ** 2 + b ** 2
c2 = math.sqrt(c1)
print("The value of c is:", c2)

#Loops inherently begin at zero
#ten times means zero to nine
for number in range(3):
    print("hello")
for number in range(1, 4):
    print("goodbye")

#loops with initial and final values
#print all multiples of 6 from 1 to 100
for i in range(1, 101):
    if i % 6 == 0:
        print(i)

#add a step value here
for i in range(0, 21):
    if i % 8 == 0:
        print(i, "is divisible by 8")
    else:
        print(i, "is not divisible by 8")

#step values
for i in range(0, 50, 3):
    if i % 5 == 0:
        print(i, "is divisible by 5")
    else:
        print(i, "is not divisible by 5")

#print after loop
for i in range(1, 20):
    if i % 5 == 0:
        print(i, "is great")
    else:
        print(i, "is not great")
print("hello world")

#between 1-100 except for numbers between 40 to 60.
for i in range(1, 101):
    if i > 20 and i < 40:
        continue
    elif i % 6 == 0:
        print(i)