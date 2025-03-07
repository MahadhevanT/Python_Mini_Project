#write program using randomisation in the python of heads and tails
import random

random_num=random.randint(0,1)
if random_num==1:
    print(f"Head is random number is {random_num}")
else:
    print(f"Tail is random number is {random_num}")

#write the Banker Roulette bill
#option 1
friends=["Alice","Bob","Charlie","David","Emanual"]
random_num2=random.randint(0,4)
print(friends[random_num2])
#option2
#this random choice function is random element in the list
print(random.choice(friends))