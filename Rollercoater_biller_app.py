height = int(input("Welcome to the Ultimate Rollercoaster!\nHow tall are you in cm?\n"))
bill = 0
if height >= 120:
    age = int(input("You can proceed!\nWhat is your age?\n"))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want photo taken? Type Y for YES or N for NO.\n")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry! Please grow taller first. Haha!")