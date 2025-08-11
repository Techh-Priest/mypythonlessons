        # Higher Lower

from art import logo4, vs

from game_data import data
import random
import os

def clear():
    os.system('cls')

def lets_play():
                game_run = True
                points = 0
                compare_b = random.choice(data)
                while game_run == True:
                        compare_a = compare_b
                        compare_b = random.choice(data)
                        while compare_a == compare_b:
                                compare_b = random.choice(data)

                        followers_a = compare_a['follower_count']
                        followers_b = compare_b['follower_count']
                        print("Welcome to André's Higher Or Lower Game!")
                        print(logo4)
                        answer = input(
                        f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}\n{vs}\nAgainst B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}\nWho has more followers? Type A or B:\n").lower()

                        def compare(guess, a_followers, b_followers):
                                if a_followers > b_followers:
                                        return guess == "a"
                                else:
                                        return guess == "b"
                        is_correct = compare(answer, followers_a, followers_b)

                        if is_correct == True:
                                clear()
                                points += 1
                                print(f"You are correct. Your score: {points}.")
                        else:
                                print(f"Game over! You are wrong. Your final score: {points}")
                                game_run = False
lets_play()