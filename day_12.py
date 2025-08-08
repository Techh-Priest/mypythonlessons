        ##### Scope ######
#enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Local scope - Exists within a function

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
#
# print(potion_strength) # This has a name error. Potion_strenght variable exists
        # and is only valid wthin the drink_potion function.

        # global scope

# player_health = 10 # this is a global variable and can be used within functions.
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#     print(player_health)
# drink_potion()


#       Block scope- Python has no block scope
# game_level = 3
# enemies = ["skeletons", "zombies", "aliens"]
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
# print(new_enemy) #This line is invalid because new_enemy only exist within the
# create enemy function.

# How to modify variable within the global scope

# enemies = 1
# def increase_enemies():
#             #global enemies # This line of code enables you to tap to a variable outside the function
#             # which specified elsewhere in the code. In this case, the enemies outside this function.
#             # Using the global scope is still not the best way. Its better  to use the return statements.
#
#             #enemies = "zombie"  # this is a completely different variable
#             # from the enemies variable above.
#             # It's a terrible idea to have two different variable with the same name.
#             print(f"enemies inside function: {enemies}")
#             return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

        ## Python Constants
# Global constants are variable which once defined,
        # you never plan on changing them ever again within your code. E,g Pi = 3.14159

# Global consants are named using uoercase letters, for example:
# PI = 3.14159
# URL = "https://www.google.com"
# GITHUB_HANDLE = "https://github.com/Techh-Priest"
# The capiatlisation of global variable enables you to know and differentiate them from other variables.
import random
import os

def clear():
    os.system('cls')
def game():
    CORRECT_NUMBER = random.randint(1, 100)
    def easy():
        lives = 10
        guessed_number = int(input(f"You have {lives} attempts remaining to guess the number.\nMake a guess:\n"))
        while lives > 0:
            if guessed_number != CORRECT_NUMBER and lives == 0:
                print(f"Game Over! The correct number is {CORRECT_NUMBER}.")
                # play_again = input("Would you like to play again? Type 'y' for yes or 'n' for no:\n").lower()
                # if play_again == "y":
                #     clear()
                #     game()
            elif guessed_number == CORRECT_NUMBER:
                print(f"You win! {guessed_number} is correct!")
                lives = 0
                play_again = input("Would you like to play again? Type 'y' for yes or 'n' for no:\n").lower()
                if play_again == "y":
                    clear()
                    game()
                else:
                    print("See you next time!")
            elif guessed_number > CORRECT_NUMBER:
                lives -= 1
                guessed_number = int(input(f"{guessed_number} is too high. You have {lives} attempts remaining. Try again:\n"))
            elif guessed_number < CORRECT_NUMBER:
                lives -= 1
                guessed_number = int(input(f"{guessed_number} is too low. You have {lives} attempts remaining. Try again:\n"))


    def hard():
        lives = 5
        guessed_number = int(input(f"You have {lives} attempts remaining to guess the number.\nMake a guess:\n"))
        while lives > 0:
            if lives == 0:
                print(f"Game Over! The correct number is {CORRECT_NUMBER}.")
                # play_again = input("Would you like to play again? Type 'y' for yes or 'n' for no:\n").lower()
                # if play_again == "y":
                #     clear()
                #     game()
            elif guessed_number == CORRECT_NUMBER:
                print(f"You win! {guessed_number} is correct!")
                lives = 0
                play_again = input("Would you like to play again? Type 'y' for yes or 'n' for no:\n").lower()
                if play_again == "y":
                    clear()
                    game()
                else:
                    print("See you next time!")
            elif guessed_number > CORRECT_NUMBER:
                lives -= 1
                guessed_number = int(input(f"{guessed_number} is too high. You have {lives} attempts remaining. Try again:\n"))
            elif guessed_number < CORRECT_NUMBER:
                lives -= 1
                guessed_number = int(input(f"{guessed_number} is too low. You have {lives} attempts remaining. Try again:\n"))

    print("Welcome to Andre's Number Guessing Game.")
    level = input("I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard.'\n").lower()
    if level == "easy":
        easy()
    elif level == "hard":
        hard()
    else:
        print("Invalid choice. Choose a valid difficulty level.")
game()