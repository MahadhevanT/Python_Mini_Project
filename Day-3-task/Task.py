#Conditional Statement
#if| else #syntax
#if condition:
#   do this
 #   else:
#   do this
#task 1-----pause-1,pause--3
#Nested if|else
#Multiple if stmt
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0
if height>=120:
    print("You can ride the rollercoaster")
    age = int(input("Enter the age? "))
    if age<=12:
        bill=5
        print("Pay $5")
    elif age<=18:
        bill=7
        print("Pey $7")
    elif age>=45 and age<=55:
        print("Everything is going to be oK.")
    else:
        bill=12
        print("Pay $12")

    photo=input("Do you want photo to take? type y for Yes n for No.")
    if photo=="y":
        bill+=3

    print(f"Your bill is ${bill}")
else:
    print("Sorry,you have grow taller before you can ride")

#Check whether the number is odd or even---pause-2
num=int(input("Enter the number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")
