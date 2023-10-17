print("wellcome to the pizza deliveries")
size = (input("choice size of the pizza:S,M or L :"))
add_pepperoni = (input("do you want pepperoni ? Y or N :"))
extra_cheese = (input("do you want extra cheese? Y or N :"))
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 25
else:
    bill += 35
if add_pepperoni == "Y":
    if size == "s":
        bill += 2
    else:
        bill += 3
        if extra_cheese == "Y":
            bill += 5

print(f"your fainal bill is :${bill}")
