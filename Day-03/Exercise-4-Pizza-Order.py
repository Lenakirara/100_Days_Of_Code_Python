"""  
Congratulations, you've got a job at Python Pizza. Your first job is to
build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price = price + 2
    else:
        price = price
        if extra_cheese == "Y":
            price = price + 1
        else:
            price = price
elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
    else:
        price = price
        if extra_cheese == "Y":
            price += 1
        else:
            price = price
else:
    price = 25
    if add_pepperoni == "Y":
        price += 3
    else:
        price = price
        if extra_cheese == "Y":
            price += 1
        else:
            price = price

print(f"Your final bill is: ${price}.")
