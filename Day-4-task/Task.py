#Random Module and function
#Example a car company many different branch of work compare random module
import random
import My_module
#to give the whole number are integer
num=random.randint(1,10)
print(num)

print(My_module.My_fav_number)

#to give the float point value random function
#does need the input for random function
#this function random_value 0 to 1 float point
float_value_0to1=random.random()*10
print(float_value_0to1)

#to give the float point value random function can give input
value_float=random.uniform(1,10)
print(value_float)

#Lists Concept of python list
#start with square brackets and end with square bracket []
fruit=["apple","banana","grapes","oranges"]
#print
print(fruit[1])

#Add the content
fruit.append("pear")

print(fruit)

#Nested List
fruit1=["apple","banana","grapes","oranges"]
Vegetable=["Carrot","tomato","potato"]

Dozen=[fruit1,Vegetable]
#print the nested lists
print(Dozen)
print("gg")
print(Dozen[1][2])
