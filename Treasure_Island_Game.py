# Lesson One: Conditional Statements(IF, ELSE, ELIF, AND, NOT)
# In Python the indentation is very important! Take note of the indentation of the if, the print function and the
# else statement.
# The following are the comparison operators= <, <=, >, >=, == and !=.
# == means specifically equal to.
# != means NOT equal to

#height = int(input ("Welcome to the Ultimate Rollercoaster!\nHow tall are you in cm?\n"))
#if height >= 120:
#    print("You can proceed!")
#else:
#    print("Sorry! Please grow taller first. Haha!")

#Creating an EVEN/ODD NUMBER CHECKER APP! Using the Modulo (%) operator
# A modulo operator gives the remainder of a division operation. See the example below which gives 1 as the answer.
# print(7 % 2) # here answer is 1.
# print(6 % 2) #Here answer is zero. So all even numbers have a modulo result of zero while odd numbers have
# a value greater than or less than 0. Let's use this knowledge to create our app below:

#number = int(input("Which number would you like to check?\n"))
#if number == 0:
#    print("This is an even number.")
#else:
#    print("This is an odd number.")

# Let's look at Nested IF & ELIF statements. Let's go back to our Rollercoater example:

#height = int(input("Welcome to the Ultimate Rollercoaster!\nHow tall are you in cm?\n"))
#if height >= 120:
#    age = int(input("You can proceed!\nWhat is your age?\n"))
#    if age < 12:
#        print("Please pay $5")
#    elif age <= 18:
#        print("please pay $7.")
#    else:
#        print("Please pay $12.")
#else:
#    print("Sorry! Please grow taller first. Haha!")



#BMI = weight in KG divided by height squared in meters

#print("Hello! Welcome to the BMI Calculator")
#weight = input("How much do you weigh in KGs?\n")
#height = input("How tall are you?\n")

#new_weight = int(weight)
#new_height = float(height)

#BMI = new_weight/new_height ** 2
#rounded_BMI = int(BMI)
#print(rounded_BMI)

#if rounded_BMI < 18.5:
#    print(f"Your BMI is {rounded_BMI}.\nYou have underweight.")
#elif rounded_BMI < 25:
#        print(f"Your BMI is {rounded_BMI}.\nYou have normal weight.")
#elif rounded_BMI < 30:
#        print(f"Your BMI is {rounded_BMI}.\nYou are overweight.")
#elif rounded_BMI < 35:
#        print(f"Your BMI is {rounded_BMI}.\nYou are obese.")
#else:
#    print(f"Your BMI is {rounded_BMI}.\nThis is serious! You are clinically obese.")



#Leap Year Challenge:
##Figure out the logic first always!!! Multiple IF STATEMENTS

#year = int(input("Welcome to the Leap Year Checker App.\nWhich year would you like to check?\n"))

#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print("This is a leap year.")
#        else:
#            print("This is not a leap year.")
#    else:
#        print("This is a leap year.")
#else:
#    print("This is not a leap year.")

#height = int(input("Welcome to the Ultimate Rollercoaster!\nHow tall are you in cm?\n"))
#bill = 0
#if height >= 120:
#    age = int(input("You can proceed!\nWhat is your age?\n"))
#    if age < 12:
#        bill = 5
#        print("Please pay $5")
#    elif age <= 18:
#        bill = 7
#        print("please pay $7.")
#    else:
#        bill = 12
#        print("Please pay $12.")

#    wants_photo = input("Do you want photo taken? Type Y for YES or N for NO.\n")
#    if wants_photo == "Y":
#        bill += 3
#    print(f"Your final bill is ${bill}.")
#else:
#    print("Sorry! Please grow taller first. Haha!")

#Pizza Orders Coding Challenge
#print("Welcome to TechPriest Pizza Deliveries!")
#size = input("What size pizza do you want? Please type:\nS for Small\nM for Medium\nL for Large\n")
#add_pepperoni = input("Do you want pepperoni? Please type:\nY for Yes or N for No\n")
#extra_cheese = input("Do you want extra cheese? Please type:\nY for Yes or N for NO\n")
#bill = 0

#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#else:
#    bill += 25
#if add_pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else:
#        bill += 3
#if extra_cheese == "Y":
#    bill += 1
#    print(f"Your final bill is ${bill}. Thank you. Enjoy!")
#else:
#    print(f"Your final bill is ${bill}. Thank you. Enjoy!")

#Let's Now look at the following logical operators: AND, OR, NOT
# When you use an AND logical operator the TWO conditions you are checking for have to be TRUE for
# the assigned/intended action to be carried out. For example A & B have to be true.

#When you use the OR operator, only one of the two conditions that you are checking for have to be true.

#The NOT operator reverses a true condition to false.
# E.g if a = 12, and I say NOT a > 15, this becomes true.

#height = int(input("Welcome to the Ultimate Rollercoaster!\nHow tall are you in cm?\n"))
#bill = 0
#if height >= 120:
#    age = int(input("You can proceed!\nWhat is your age?\n"))
#    if age < 12:
#        bill = 5
#        print("Please pay $5")
#    elif age <= 18:
#        bill = 7
#        print("please pay $7.")
#    elif age >= 45 and age <= 55:
#        print("Yay! You get a free ride on us!")
#    else:
#        bill = 12
#        print("Please pay $12.")

#    wants_photo = input("Do you want photo taken? Type Y for YES or N for NO.\n")
#    if wants_photo == "Y":
#        bill += 3
#    print(f"Your final bill is ${bill}.")
#else:
#    print("Sorry! Please grow taller first. Haha!")

#Now let's build a Love Calculator!

#print("Welcome to the Love Calcutaor!")
#name1 = input("What is your name?\n")
#name2 = input("What is their name\n")
#TRUE LOVE
#first_name = name1.lower()
#second_name = name2.lower()

#combined_names = first_name + second_name
#name= combined_names.lower()
#tru = name.count("t") + name.count("r") + name.count("u") + name.count("e")
#love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

#combined_score =  str(tru) + str(love)
#percentage = int(combined_score)

#if percentage <= 10 or percentage >= 90:
#    print(f"Your score is {percentage}%. You go together like coke and mentos.")
#elif percentage >= 40 and percentage <= 50:
#    print(f"Your score is {percentage}%. You are alright together.")
#else:
#    print(f"Your love score is {percentage}%.")

#Final Code Challenge:
#TreasureIsland App
print ('''
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
*******************************************************************************''')
print("Welcome to Treasure Island!\nYour mission is to find the treasure!")
direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

if direction == "left":
    choice1 = input("You've come to a lake. There is an island in the middle of the lake.\n"
          "Type 'wait' to wait for the boat. Type 'swim' to swim to the island\n").lower()
    if choice1 == "wait":
        choice2 = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which doors do you choose?\n").lower()
        if choice2 == "red":
            print("Its a room full of ice. Game over!")
        elif choice2 == "yellow":
            print("Yay! You found the treasure you won!")
        elif choice2 == "blue":
            print("It's a room full of fire. Game Over!")
        else:
            print("You chose a vacuum. Game Over!")
    else:
        print("You got attacked by an angry Tilapia. Game Over!")
else:
    print("You fell into a hole. Game Over!")
