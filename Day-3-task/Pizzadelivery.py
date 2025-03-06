#Pizza Delivery Program
print("Welcome to Python Pizza Deliveries!")
size=input("what size pizza do you want? S, M or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")
price=0
if size=="S":
    price=15
    #print("price is $15")
    if pepperoni=="Y":
        price+=2
    #print(f"Your final bill is: ${price}")
    if extra_cheese == "Y":
        price += 1

    print(f"Your final bill is: ${price}")
elif size=="M":
    price=20
    #print("Price is $20")
    if pepperoni=="Y":
        price+=3
    #print(f"Your final bill is: ${price}")
    if extra_cheese == "Y":
        price += 1

    print(f"Your final bill is: ${price}")
elif size=="L":
    price=25
    #print("Price is $25")
    if pepperoni=="Y":
        price+=3
    #print(f"Your final bill is: ${price}")
    if extra_cheese == "Y":
        price += 1

    print(f"Your final bill is: ${price}")
else:
    print("You have typed wrong input")