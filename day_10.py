        #More about Functions

# Functions with Outputs
# def my_function():
#     return 3 * 2
#
# output = my_function()
# print(output)

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide names."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#
# #The return keyword tells the computer, this is the end of the function.
#
# formatted_string = format_name("AndRew", "ingati")
# print(formatted_string) # or strike this and simply just do:
# print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))

        #Days in month excercise.

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# def days_in_month(year, month):
#             if month > 12 or month < 1:
#                 return "Invalid month!"
#             month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#             if is_leap(year) and month == 2:
#                 return 29
#             return month_days[month - 1]
#
#
# year = int(input("Enter a year:\n"))
# month = int(input("Enter a month:\n"))
#
#
# days = days_in_month(year, month)
# print(days)


        ## Docstrings - A way for us to create little bits of documentation as we are coding
        # along in our blocks of code.

# def format_name(f_name, l_name):
#     """Takes the first and last name and format it
#      as a properly capitalised title/noun."""
#     #Doc strings are multi-lines in contrast to strings.
#     if f_name == "" or l_name == "":
#         return "You didn't provide names."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"


            # Calculator Program

def add(n1, n2):
    """Adds two values togethger to give the sum."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two values to give the difference."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two values together"""
    return n1 * n2

def divide(n1, n2):
    """Divides two values"""
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
        }
def calculator():
    from art import logo2
    print(logo2)

    num1 = float(input("What is the first number?:\n"))

    for symbol in operations:
        print(symbol)

    to_continue = True
    while to_continue == True:

        operation_symbol = input("Pick an operation:\n")
        num2 = float(input("What is the next number?:\n"))

        # if operation_symbol == "+":
        #     first_answer = add(num1, num2)
        # elif operation_symbol == "_":
        #     first_answer = subtract(num1, num2)
        # elif operation_symbol == "*":
        #     first_answer = multiply(num1, num2)
        # elif operation_symbol == "/":
        #     first_answer = divide(num1, num2)
        # else:
        #     print("Please choose a valid symbol.")

            # Instead of the many long if statements you can just do:
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation:\n") == "y":
            num1 = answer
        else:
            to_continue = False
            calculator()

calculator()
