import random
import hangman_words
import hangman_art

lives = 6
end_of_game = False
display =[]



print(f"{hangman_art.logo}Welcome To André's Hangman Game!\nAndré's Hangman Game is a word game in which the player is trying to guess a secret word.\nThe player guesses letters, one at a time, and is told where each such letter appears in the secret word.")

chosen_word = random.choice(hangman_words.word_list)
chosen_list = list(chosen_word)

# for letter in chosen_word:
#     if guess == letters:
#         print("Right")
#     else:
#         print("Wrong")

for letter in chosen_word:
    display.append("_")
print(display)

while end_of_game == False:

    guess = input("Guess a letter for the above word:\n").lower()



    if guess in display:
        print(f"You've already guessed {guess}. Try again.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    print(hangman_art.hangman_guy[lives])