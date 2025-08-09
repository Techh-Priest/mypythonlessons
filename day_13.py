        # Debugging
# Grace Hopper was the first debugger where a literal moth was in her
        # relay that prevented the code from running properly.

############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20): # Change this to 21. Check the range function.
#       if i == 20:
#           print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # simply change this to randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?\n"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?\n"))
# if age > 18:
#             print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages:\n "))
# word_per_page = int(input("Number of words per page:\n"))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger like thonny
# def mutate(a_list):
#             b_list = []
#             for item in a_list:
#                 new_item = item * 2
#                 b_list.append(new_item)
#             print(b_list)
#
# mutate([1,2,3,5,8,13])

        # Debug odd or even exercise
# number = int(input("Which number do you want to check?:\n"))
#
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

        # Debug Leap Year Exercise
# year = int(input("Which year do you want to check?:\n"))
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
#     print(f"{year} is not a leap year.")

        # Debug Fizz Buzz Exercise
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    else:
        print(number)