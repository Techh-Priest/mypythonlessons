                #Randomisation/Random Module
# This is important in creating programs with a degree of unpredictability. Very useful in games btw.
# Computers are deterministic and will perform repeatable actions in a predictable way.
# Python uses a pseudo random number generator called the Mersenne Twister.


# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# What exactly is a python module? When you have a complex and long line of code, you split the code up in different modules where each module
# is responsible for a specific functionality in your program. This allows for collaboration where different people work on different mudules.
# main.py is the file that is executed when we run our code.

# import my_module
# print(my_module.pi) ## These two lines of code show how you can import a module in your main.py file/program.


# import random
# random_float = random.random()
# print(round(random_float * 5, 1))

        # Heads or Tails Program

# import random
# random_integer = random.randint(0, 1)
#
# if random_integer == 0:
#     print("Heads")
# else:
#     print("Tails")






            ## Python Lists
  #This is simply a data structure. A way to store grouped pieces of data that usually have
  # some sort of connection to each other e.g names of counries. Also it helps faciliate order for example
  # in a virtual queue.

# fruits = ["mango", "orange", "melons", "pineapple", "apple", "paw paws"]
# In a list you can store and data type and even mix up the stored date types.

#states_of_USA = ["Delaware", "Pennsylvania", "Illinois", "Florida"]
#print(states_of_USA[0]) # this prints Delaware as item zero in the list. Counting in python starts at zero. Item 1 is Pennsylavia.
# You can also save an item inside a list in a variable for example:
#home_state = states_of_USA[2] #this has save Illinois in the home_state variable.
#print(home_state)

# You can also use a negative index which will start pulling items from the end of the list.
#print(states_of_USA[-1]) #This gives Florida.

#You can also change items in the list:
#states_of_USA[1] = "Pencilvania"
#print(states_of_USA)

#You can also add items in the list using the append function:
#states_of_USA.append("Andrew Land")
#print(states_of_USA)

#You can also add multiple items in a list using the extend funtion basically adding a list on your existing list:
#states_of_USA.extend(["Paris", "Rome", "Monaco"])
#print(states_of_USA)


            ## Banker Roulette

# names_string = input("Give me everyone's names, separated by a comma.\n")
# names = names_string.split(", ")
# #['angela', 'andrew', 'ben', 'jenny']
# list_total = len(names)
#
# import random
# lucky_num = random.randint(0, list_total - 1)
# lucky_person = names[lucky_num]
# print(f"{lucky_person} is going to buy the meal today. Congratulations, {lucky_person}!")


    #### Index Errors & Working with Nested Lists

#since counting in lists starts at 0, yet the len() function starts counting at one to give the exact items in the list,
# be careful of an index out of range error.
#fruits = ["apple", "orange", "mango", "melon"]
#print(fruits[4]) # Index out range error!!!!! To correct this do: print(fruits[4 - 1])

# A nested list is a list within a list.

#boys = ["Ken", "Tom", "Kev", "John"]
#girls = ["Mary", "Jenny", "Lulu", "Elsie"]

#people = [boys, girls]

#print(people) # Prints a list within a list. Take note of the brackets.


    # Treasure Map Exercise

# row_1 = ["😁", "😎", "🥴"]
# row_2 = ["😪", "😈", "🤥"]
# row_3 = ["🤪", "🤯", "😭"]
#
# map = [row_1, row_2, row_3]
# print(f"{row_1}\n{row_2}\n{row_3}")
#
# position = input("Where do you want to put the treasure?\n")
#
# column = int(position[0])
# row = int(position[1])
#
# selected_row = map[row - 1]
# selected_row[column - 1] = "X"
#
# print(f"{row_1}\n{row_2}\n{row_3}")


            ### Rock Paper Scissors Game Project
    #Official Game Rules
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
      _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
        _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(f"{rock}\n{paper}\n{scissors}")
print("Welcome to Andre's Rock Paper Scissors Game!")
user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


import random
computer_choice = random.randint(0, 2)
# Rock(0) wins against scissors.
# Paper(1) wins against rock.
# Scissors(2) win against paper.

if user_choice == 0 and computer_choice == 1:
    print(f'''You chose Rock:\n{rock}.\nThe computer chose Paper:\n{paper}.\nThe computer won.''')
elif user_choice == 0 and computer_choice == 2:
    print(f'''You chose Rock:\n{rock}.\nThe computer chose Scissors:\n{scissors}.\nYou won.''')
elif user_choice == computer_choice:
    print("Draw. Both you and the computer chose the same.")
elif user_choice == 1 and computer_choice == 0:
    print(f'''You chose Paper:\n{paper}.\nThe computer chose Rock:\n{rock}.\nYou won.''')
elif user_choice == 1 and computer_choice == 2:
    print(f'''You chose Paper:\n{paper}.\nThe computer chose Scissors:\n{scissors}.\nThe computer won.''')
elif user_choice == 2 and computer_choice == 0:
    print(f'''You chose Scissors:\n{scissors}.\nThe computer chose Rock:\n{rock}.\nThe computer won.''')
elif user_choice == 2 and computer_choice == 1:
    print(f'''You chose Scissors:\n{scissors}.\nThe computer chose Paper:\n{paper}.\nYou won.''')
else:
    print("Invalid Choice. Try again.")
