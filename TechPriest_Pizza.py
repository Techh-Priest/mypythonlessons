#Pizza Orders Coding Challenge
print("Welcome to TechPriest Pizza Deliveries!")
size = input("What size pizza do you want? Please type:\nS for Small\nM for Medium\nL for Large\n")
add_pepperoni = input("Do you want pepperoni? Please type:\nY for Yes or N for No\n")
extra_cheese = input("Do you want extra cheese? Please type:\nY for Yes or N for NO\n")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is ${bill}. Thank you. Enjoy!")
else:
    print(f"Your final bill is ${bill}. Thank you. Enjoy!")