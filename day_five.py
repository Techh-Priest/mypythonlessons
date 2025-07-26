            ### Loops

#Things that have to happen repeatedly many time.
#First type of loop is a For Loop

#for item in list_of_items:
    #Do something to each item in the list

# fruits = ["apple", "mango", "peach"]
# for fruit in fruits: #In a For Loop, you give variable called fruit which will be assigned for each item in the list as long as the list and loop runs
#     print(fruit)
#     print(fruit + "pie")
# print(fruits) # this will print after the For Loop is done.

            ## Code Challenge

# student_heights = input("Enter a list of student heights.\n").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
#
# number_of_students = 0
# for students in student_heights:
#     number_of_students += 1
# print(number_of_students)
#
# average_height = round((total_height / number_of_students), 2)
# print(average_height)


    ## Code Exercise
#
# student_scores = input("Enter a list of scores.\n").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

    ##For Loops & The Range Function

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

        #Code Challenge: Adding Evens

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)


        #Fizz Buzz Code Challenge
# number = 0
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

    # Code Challenge
import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "-", "@", "+", "%", "&", "?", "^", "/", "^", "<", ">", ",", "(", ")", "*"]


print("Welcome to André's PyPassword Generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))


# password = ""
# for char in range(1, nr_letters + 1):
#      random_char = random.choice(letters)
#      password += random_char #Or these two lines of code can be" password += random.choice(letters)
# print(password)
#
# for char in range(1, nr_numbers + 1):
#      password += random.choice(numbers)
#
# for char in range(1, nr_symbols + 1):
#      password += random.choice(symbols)

#print(password) #This is the easy level solution.
            # Now, how can you print out this password whereby the numbers, ketters and symbols
            # are mixed up at random? Hard level is below:


password_list = []
for char in range(1, nr_letters + 1):
     random_char = random.choice(letters)
     password_list += random_char #Or these two lines of code can be" password += random.choice(letters)

for char in range(1, nr_numbers + 1):
     password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
     password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}.")