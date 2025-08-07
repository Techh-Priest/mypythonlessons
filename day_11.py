        # Blackjack/21 Capstone Project
import random
import os
from art import logo3
print(logo3)

## *******      My Work Starts Here          ******************

# def player_cards():
#                 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#                 start_game = input("Do you want to play a game of Andre's BlackJack? Type 'y' for yes or 'n' for no.\n").lower()
#                 game_run = True
#                 while game_run == True:
#                         user_choice1 = random.randint(1, 12)
#                         user_choice2 = random.randint(1, 12)
#                         user_card1 = cards[user_choice1]
#                         user_card2 = cards[user_choice2]
#                         user_score = user_card1 + user_card2
#
#                         comp_choice1 = random.randint(1, 12)
#                         comp_choice2 = random.randint(1, 12)
#                         comp_card1 = cards[comp_choice1]
#                         comp_card2 = cards[comp_choice2]
#                         comp_score = comp_card1 + comp_card2
#                         if comp_score == 21 and user_score < 21:
#                                 print("Computer wins!")
#                                 game_run = False
#                         elif user_score == 21 and comp_score < 21:
#                                 print("You win!")
#                         elif start_game == "n":
#                                 game_run = False
#                         print(f"Your cards:[{user_card1}, {user_card2}], Current score: {user_score}")
#                         print(f"Computer's first choice: {comp_card1}")
#
#                         continue_game = input("Type 'y' to get another card or 'n' to pass:\n")
#                         if continue_game == "n":
#                                 player_cards()
#                                 game_run = False
#                         else:
#                                 user_choice3 = random.randint(1, 12)
#                                 user_card3 = cards[user_choice3]
#                                 user_score += user_card3
#                                 print(f"Your cards:[{user_card1}, {user_card2}, {user_card3}], Current score: {user_score}")
#
#
# player_cards()


## *******      My Work Ends Above This Line. Failed The Logic!!!!         ******************
def clear():
    os.system('cls')

def deal_card():
        """Returns a random card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

def calculate_score(cards):
        """Take a list of cards and return the score calculated from cards"""
        if sum(cards) == 21 and len(cards) == 2:
                return 0
        if 11 in cards and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)
        return sum(cards)
def compare(user_score, comp_score):
        if user_score == comp_score:
                return "Draw"
        elif comp_score == 0:
                return "You lose! Opponent has a blackjack"
        elif user_score == 0:
                return "You win with a blackjack!"
        elif user_score > 21:
                return "You went over. You lose!"
        elif comp_score > 21:
                return "Opponent went over. You win!"
        elif user_score > comp_score:
                return "You win!"
        else:
                return "You lose!"
def play_game():
        user_cards = []
        comp_cards = []
        is_game_over = False

        for _ in range(2):
                user_cards.append(deal_card())
                comp_cards.append(deal_card())

        while is_game_over == False:
                user_score = calculate_score(user_cards)
                comp_score = calculate_score(comp_cards)
                print(f"Your cards: {user_cards}. Current score: {user_score}")
                print(f"Computer's first card: {comp_cards[0]}")

                if user_score == 0 or comp_score == 0 or user_score > 21:
                        is_game_over = True
                else:
                        user_should_deal = input("Type 'y' to get another card. Type 'n' to pass:\n")
                        if user_should_deal == "y":
                                user_cards.append(deal_card())
                        else:
                                is_game_over = True

        while comp_score != 0 and comp_score < 17:
                comp_cards.append(deal_card())
                comp_score = calculate_score(comp_cards)

        print(f"Your final hand: {user_cards}. Your final score: {user_score}")
        print(f"Computer's final hand: {comp_cards}. Computer's final score: {comp_score}")
        print(compare(user_score, comp_score))

while input("Do you want to play Andre's Blackjack? Type 'y' for yes, or 'n' for no:\n") == "y":
        clear()
        play_game()