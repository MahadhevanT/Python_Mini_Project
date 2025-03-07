#Rock,Paper and Scissors Game
Rock='''
    _______
___'   ____)
      (______)
      (______)
      (____)
---'__(___)

'''
Paper= '''
    ________
___'   ____)____
         _______)
         ________)
        ________)
---._________)
'''
Scissors= '''
    _______
___'    ___)____
         _______)
      ___________)
      (____)
---.__(___)
'''

import random

game=[Rock,Paper,Scissors]
choice1=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choice1>=0 and choice1<=2:
    print(game[choice1])
random_num=random.randint(0,2)
print(f"Computer Chose: {random_num}")
print(game[random_num])
if choice1 >=3 or choice1<0:
    print("You typed invalid number.You Lose!")
elif choice1==0 and random_num==2:
    print("You Win!")
elif choice1==2 and random_num==1:
    print("You Win!")
elif choice1==1 and random_num==0:
    print("You Win!")
elif choice1==random_num:
    print("It is Draw!")
else:
    print("You Lose!")