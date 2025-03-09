#For loops
#Syntax:for item in list_item:
fruits=["apple","mango","banana","oranges"]
for fruit in fruits:
    print(fruit)

#Example 1
Student_Score=[100,150,145,142,160,126,55,85,200]
total=sum(Student_Score)
print(total)

#how built-in function work
"""temp=0
for score in Student_Score:
    temp+=score
print(temp)
"""
#find the max element in list
tot=max(Student_Score)
print(tot)
temp=0
for score in Student_Score:
    if temp<score:
        temp=score
print(temp)

#Add the number from 1 to 100
temp=0
for num in range(1,101):
    temp+=num
print(temp)

# range function
for numm in range(1,10+1):
    print(numm)


##
import random

my_string = "helloworld"
char_list = list(my_string)
print(char_list)
random.shuffle(char_list)
randomized_string ="".join(char_list)
print(randomized_string)



import random

my_string = "helloworld"
shuffled_string = ''.join(random.sample(my_string, len(my_string)))
print(shuffled_string)