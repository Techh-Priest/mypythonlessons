# counting in python begins at 0. In a string you can actually pull out a
# specific character(s) from a string individually by using these brackets:[] and inserting
# the position of the character we want. In order to pull out h from below we use its index
# postion of zero/0.1
# len function usually works with the string data type
# type function is used to investigate the type of data type we are dealing with.

#print("hello"[4])
#In real life we use commas for large number for readability e.g 1,000,000.
#In python we use underscores as a replacement for real-life commas. e.g 1,000,000 would be 1_000_000.
#Run the code below:
#print(1_000 + 2_000)

#Here is a small program that gives the sum of any two-digit number.
#choosen_number = input("Hello and welcome! Type a random two-digit.\n")
#sum_of_rand = int(choosen_number[0]) + int(choosen_number[1])
#print(sum_of_rand)

#Any number that is as a result of the division operation, the result will always be a float.
# two asterixs in python meaning raising a number to a specified number e.g:
#print(2**3) # this gives 8.


#BMI = weight in KG divided by height squared in meters

#print("Hello! Welcome to the BMI Calculator")
#weight = input("How much do you weigh in KGs?\n")
#height = input("How tall are you?\n")

#new_weight = int(weight)
#new_height = float(height)

#BMI = new_weight/new_height ** 2
#rounded_BMI = int(BMI)
#print(rounded_BMI)


#print (8/3) #This gives a float data type as the resulting value with many decimal places
#print (round(8/3)) #using the round funtion we can round the number to the closest whole number. The resulting value is an integer.
#print (round(8/3, 2)) #The , 2 is used with the round function to specify the number of decimal places you want your result to have. In this case 2.

#print (8 // 3) #The two // symbolize the floor function which gives an integer result and a whole number.
#random example below:
#result = 4 / 2
#result /= 2
#print(result)

#Lets say you are keeping a score that increases by one point everytime:
#score = 0
#score += 1 #Take note of /= and += and -= and *= operations
#print(score)



#f-strings is used to mix string and different data types
#score = 1
#print("Your score is " + score) #this gives you an error because we are trying to concatenate different data types.
# Instead of coverting the score into a string data type with str(score), here is where an f-string become useful as shown below:
#score = 0 #this is an integer
#height = 1.8 # This is a float
#isWinning = True #this is a boolean

#print(f"Your score is {score},\nYour height is {height},\nYou are winning is {isWinning}")


#life in weeks calculator:
#age = int(input("Considering you live up to 90 years of age,\nlets calculate how much time you have left.\nWhat is your current age?\n"))
#years_left = 90 - age
#weeks_left = years_left * 52
#months_left = years_left * 12
#days_left = years_left * 365

#print(f"You have {days_left} days,{weeks_left} weeks and {months_left} months left")

#Final Project for this lesson: The Tip Calculator! Let's go!
bill = int(input ("Welcome to the Tip Calculator.\nWhat was the total bill?\n"))
percentage_tip = int(input("What percentage tip would you like to give?\n"))
number_of_people = int(input("How many people are splitting the bill?\n"))

tip = bill * (percentage_tip/100)
total_bill = bill + tip
divided_bill = round(total_bill // number_of_people, 2)
formatted_bill = "{:.2f}".format(divided_bill)
print(f"Each person should pay: {formatted_bill}.\nThank you for eating with us!")