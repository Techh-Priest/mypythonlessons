#         #More About Functions
# # def greet():
# #     print("Hello!")
# #     print("How are you?")
# #     print("How do you do?")
# #
# # greet()
# #     #Now we can create a function that allows for input
# # def greet_with_name(name):
#
# #     print(f"Hello {name}!")
# #     print(f"How are you {name}?")
# #     print(f"How do you do, {name}?")
# #
# # greet_with_name("Andrew")
#
#         #Functions with more than one input below:
#
# # def greet_with(name, location):
# #     print(f"Hello {name}!")
# #     print(f"What is it like in {location}?")
# #
# # greet_with("Andrew", "Nairobi") #This is the default way to call functions AKA
#                                 # positional arguments.
#
# # def greet_with(name, location):
# #      print(f"Hello {name}!")
# #      print(f"What is it like in {location}?")
# #
# # greet_with(name = "Andrew", location = "Nairobi") #This time if you switch the arguments
# # #                                                     # nothing happens.
#
#         ## Paint Area Calc Challenge
#

# # import math
# # def paint_calc(height, width, cover):
# #     area = height * width
# #     cans = math.ceil(area / cover)
# #     print(f"You'll need {cans} number of cans of paint.")
# #
# # test_h = int(input("Height of wall:\n"))
# # test_w = int(input("Width of wall:\n"))
# # coverage = 5
# #
# # paint_calc(height=test_h, width=test_w, cover=coverage)
#
#         #Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number")
#
# n = int(input("Check this number:\n"))
# prime_checker(number=n)


        #### Caesar Cipher Encoding
from art import logo
print(logo)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b",
            "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' to go again. Otherwise, type 'no'.\n").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye.")

#The two functions below along with the IF statement are all simplified and bundled
# in the above Caesar function. Neat!!

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}.")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Error! Please type 'encode' or 'decode'.")

