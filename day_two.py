# # Data Types:
# #     String -
# #     interger
# #     Boolean
# #     float
# #
# # print("hello"[4]) #Pulling a particular element from a string like this is called subscripting.
# # "123" is treated as a string in python
# # if you print print(123 + 100) this is an integer and the code will give you a sum.
# # If you put commas or underscores in between large numbers, it will understood by python as a usual real world number e.g
# # 1,984,000 is same as 1_984_000 which is same as 1984000.
# # Float is just a number with a decimal point.
# # Boolean has just two possible values: True or False. The capitalization is important.
# #
# # You can never concatenate/join a string and an integer.
# #
# # The type() function is used to find out the data type of anything in python. For example look below:
# #
# # print(type(2))
# # print(type("Hello"))
# #
# # Additionally, you can change/convert between date types like below:
# #
# # x = "hello"
# # str(x)
# # print(type(x))
# #
# # y = 3000
# # int(y)
# # print(type(y))
#
# a = 406
# print(float(a)) #this give a value of 406.0. Now lets convert it back to a string:
# print(str(a))

#print(70 + float("100.5")) #This gives 170.5 because addition or operations between a float and an integer is possible.
#print(str(70) + str(100)) #This gives 70100 because after string conversion it just joins the values together.

#two_digit_num = input("Type a two-digit number\n")

#print(int(two_digit_num[0]) + int(two_digit_num[1]))

#Division in Python gives a float result

#Using two asterix means raising a number to the power E.g => 2 ** 2 gives 4.

#PEMDASLR is the order by which mathematical operations are done in Python
#PEMDASLR = Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction with the priority operation being done
# from Left to Right, hence PEMDASLR.


# BMI CODE EXERCISE 1.0
#BMI = Weight(kg)/height Squared in Meters

#height = input("What's your height in meters?\n")
#weight = input("What's your weight in kg\n")

#w = int(weight)
#h = float(height)

#h_squared = h ** 2
#BMI = w / h_squared
#print(int(BMI))


#Rounding in Python using the Round Function

#print(round(8 / 3, 2)) #The 2 here specifies the number of decimal places you want the result to be rounded to.
#print(8 // 3) #This // sign gives only a rounded number and the result is an interger and NOT a float. This is called a
# floored division sign. Floored division gives an integer.

#F Strings for printing enables you to print all data at the same time without converting them to the same data type e.g:
#score = 10
#isWinning = True
#print(f"Your score is {score}. You are winning is {isWinning}!")

#F strings helps you to avoid a lot of the manual labor involved in type conversion when printing.

#Code Exercise

#age = input("How old are you right now?\n")

#years_left = 90 - int(age)

#months_left = years_left * 12

#weeks_left = years_left * 52

#days_left = years_left * 365

#print(f"You have {years_left} years, {months_left} months, {weeks_left} weeks and {days_left} days left on this earth")

#Tip Calculator App

bill = input("Welcome to the Tip Calculator\nWhat was the total bill?\n")
tip_percentage = input("What percentage tip would you like to give?\n10%, 12% or 15%\n")
no_of_people = input("How many people to split the bill?\n")

tip = round(float(bill)*int(tip_percentage)/100, 2)

total_bill = float(bill) + tip

bill_portions = round(float(total_bill)/int(no_of_people), 2)
formatted_bill_portions = "{:.2f}".format(bill_portions)
print(f"Each person should pay: ${formatted_bill_portions}.")