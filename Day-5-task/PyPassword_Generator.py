#password Generator
import random

let=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
syb=['!','@','#','$','%','&','*','(',')','+','^']


print("Welcome to the PyPassword Generator!")
letter=int(input("How many letters would you like in your password?\n"))
symbol=int(input("How many symbols would you like?\n"))
number=int(input("How many numbers would you like?\n"))

#Easy Level
password=""
for char in range(0,letter):
    password+=random.choice(let)
    #print(password)
for char in range(0,symbol):
    password+=random.choice(syb)

for char in range(0,number):
    password+=random.choice(num)

print(f"Your password is: {password}")

#hard Level
password=[]
for char in range(0,letter):
    password.append(random.choice(let))
    #print(password)
for char in range(0,symbol):
    password.append(random.choice(syb))

for char in range(0,number):
    password.append(random.choice(num))

#Random shuffle() to shuffle the password
random.shuffle(password)
newpassword=""
#change the list to string
for char in password:
    newpassword+=char
print(f"Your hard  password is: {newpassword}")
