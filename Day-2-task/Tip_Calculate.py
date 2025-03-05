# Tip Calculator
print("Welcome to the Tip Calculator!")
total_bill=float(input("What was the total bill?\n$"))
tip_give=int(input("How much tip would you like too give? 10%, 12% or 15%?\n"))
Head_count=int(input("How many people to split the bill?\n"))
res1=total_bill*(tip_give/100)
res2=(res1+total_bill)/Head_count
print(f"Each person should pay: \n$ {round(res2,2)}")
