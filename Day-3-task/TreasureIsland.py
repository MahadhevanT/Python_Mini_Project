# Click Run to run th final project you will build
#Treasure Island
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island!")
print("Your mission is to find the Treasure!")
direction=input("You 're at a cross road.where do you want to go?\nType \"left\" \"right\"\n").lower()
if direction=="left":
    print("You've come to lake. There is an island in the middle of the lake.")
    level=input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n").lower()
    if level=="wait":
        print("You arrive at the island unharmed.There is a house with 3 doors")
        level3=input("One red, One yellow and One blue. Which colour do you choose?\n").lower()
        if level3=="red":
            print("Burned,by fire. Game Over")
        elif level3=="blue":
            print("Eaten by Beasts.Game Over.")
        elif level3=="yellow":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("fall into a hole. Game Over")