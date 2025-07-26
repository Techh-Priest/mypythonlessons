#Python Statements
     # 1.conditional Statements: if/else
     #In Python Spacing and Indentation is part of the code and is very IMPORTANT!!.
     #   > means greater than
     #   < means less than
     #   >= means greater than or equal to
     #   <= means less that or equal to
     #   == means equal to
     #   != means not equal to


#height = int(input("Welcome to Andre's Rollercoaster.\nHow tall are you in cm?\n"))

#if height >= 120:
#    print("You can ride the rollercoaster.")
#else:
#    print("You too short!! 😅😭")


#Odd or Even Number Checker App

#number = int(input("Welcome to Odd/Even Number Checker!\nEnter number:\n"))

#if number % 2 == 0:
#    print("This is an even number.")
#else:
#    print("This is an odd number.")



      #Nested if statements and elif statements

#height = int(input("Welcome to Andre's Rollercoaster.\nHow tall are you in cm?\n"))

#if height >= 120:
#    print("You can ride the rollercoaster.")
#    age = int(input("How old are you?\n"))
#    if age < 12:
#        print("Please pay $5.")
#    elif age <= 18:#please note the indentation of the elif. You can use as many elifs as possible.
#        print("Please pay $7.")
#    else:
#        print("Please pay $12.")
#else:
#    print("Sorry, you too short!! 😅😭")




              #BMI Calculator 2.0 Code Challenge
#BMI = Weight(kg)/height Squared in Meters

# height = input("Enter your height in meters?\n")
# weight = input("Enter your weight in kg?\n")
#
# w = int(weight)
# h = float(height)
#
# h_squared = h ** 2
# BMI = int(w / h_squared)
#
# if BMI < 18.5:
#     print(f"Your BMI index is {BMI}. You are underweight.")
# elif BMI < 25:
#     print(f"Your BMI index is {BMI}. You have normal weight.")
# elif BMI < 30:
#     print(f"Your BMI index is {BMI}. You are overweight.")
# elif BMI < 35:
#     print(f"Your BMI index is {BMI}. You are obese.")
# else:
#     print(f"Your BMI index is {BMI}. You are clinically obese.")

         #Leap Year Code Challenge

# A leap year occurs when a year is divisible by 4, except for years divisible by 100, unless they are also divisible by 400.
# This logic ensures the calendar year stays aligned with the Earth's orbit around the sun.
# Here's a breakdown of the logic:
#
# Divisible by 4: If a year is evenly divisible by 4 (with no remainder), it may be a leap year.
#
# Divisible by 100: If the year is also divisible by 100, it's not a leap year, unless...
# Divisible by 400: If the year is divisible by both 100 and 400, it is a leap year.

# print("Welcome To Andre's Leap Year Checker App")
# year = int(input("Which year do you want to check?\n"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year")


        # Multiple if Conditions

# height = int(input("Welcome to Andre's Rollercoaster.\nHow tall are you in cm?\n"))
# bill = 0
#
# if height >= 120:
#    print("You can ride the rollercoaster.")
#    age = int(input("How old are you?\n"))
#    if age < 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18: #please note the indentation of the elif. You can use as many elifs as possible.
#        bill = 7
#        print("Youth tickets are $7.")
#    else:
#        bill = 12
#        print("Adult tickets are $12.")
#    wants_photo = input("Do you want a photo taken?\nType Y for Yes and N for No.\n")
#    if wants_photo == "Y":
#        bill += 3
#
#    print(f"Your final bill is ${bill}.")
# else:
#    print("Sorry, you too short!! 😅😭")



        #Logical operators in Python Statements
# There are three of them:
        # and - Used to combine two different conditions that BOTH have to be true.

        # or - Used to combine two conditions that both or ONLY ONE has to be true.
#       Only when both conditions are false, does this statement become false

        #not - Used to reverse a condtion.


# height = int(input("Welcome to Andre's Rollercoaster.\nHow tall are you in cm?\n"))
# bill = 0
#
# if height >= 120:
#    print("You can ride the rollercoaster.")
#    age = int(input("How old are you?\n"))
#    if age < 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18: #please note the indentation of the elif. You can use as many elifs as possible.
#        bill = 7
#        print("Youth tickets are $7.")
#    elif age >= 45 and age <= 55:
#        bill = 0 # Specifying bill is not compulsary. Code will still run perfectly.
#        print("Congratulations! Your ride's on us!")
#    else:
#        bill = 12
#        print("Adult tickets are $12.")
#    wants_photo = input("Do you want a photo taken?\nType Y for Yes and N for No.\n")
#    if wants_photo == "Y":
#        bill += 3
#    print(f"Your final bill is ${bill}.")
# else:
#    print("Sorry, you too short!! 😅😭")



                # Love Calculator App (LOL!!!)

# print("Welcome to Dr. Andrew GoodLove Love Calculator App")
#
# name1 = input("Enter your name.\n")
# name2 = input("Enter your love interest's name.\n")
#
# first_name = name1.lower()
# second_name = name2.lower()
#
# letter_one = first_name.count("t")
# letter_two = first_name.count("r")
# letter_three = first_name.count("u")
# letter_four = first_name.count("e")
#
# letter_nine = second_name.count("t")
# letter_ten = second_name.count("r")
# letter_eleven = second_name.count("u")
# letter_twelve = second_name.count("e")
#
# letter_five = first_name.count("l")
# letter_six = first_name.count("o")
# letter_seven = first_name.count("v")
# letter_eight = first_name.count("e")
#
# letter_thirteen = second_name.count("l")
# letter_fourteen = second_name.count("o")
# letter_fifteen = second_name.count("v")
# letter_sixteen = second_name.count("e")
#
# score_1 = str(letter_one + letter_two + letter_three + letter_four + letter_nine + letter_ten + letter_eleven + letter_twelve)
#
# score_2 = str(letter_five + letter_six + letter_seven + letter_eight + letter_thirteen + letter_fourteen + letter_fifteen + letter_sixteen)
#
# percentage = int(score_1 + score_2)
#
# if percentage < 10 or percentage > 90:
#     print(f"Your love score is {percentage}%. You go together like coke and mentos.")
# elif percentage >= 40 and percentage <= 50:
#     print(f"Your love score is {percentage}%. You are alright together.")
# else:
#     print(f"Your love score is {percentage}%.")



            # Treasure Island Game

print('''
*******************************************************************************
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
*******************************************************************************
''')

print("Welcome to Captain Andrew's Treasure Island.\nYour mission is to find the treasure.\n")
where = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'.\n")
direction = where.lower()

if direction == "left":
    how = input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across.\n")
    lake = how.lower()
    if lake == "wait":
        three_doors = input("You arrive at the island unharmed. There is a house with three doors.\nThe first one is red, second is yellow, and third is blue.\nChoose a door.\n")
        door = three_doors.lower()
        if door == "yellow":
            print("Yay, congratulations!\nYou are soo rich now!\nYou found Captain Andrew's Treasure.")
        elif door == "red":
            print("You were bitten to death! You entered a room full of snakes.")
        else:
            print("You entered a room full of sand. You have to go back empty handed.")
    else:
        print("Game over!! You were devoured by sharks.")
else:
    print("Game over! You fell in a bottomless hole.")

