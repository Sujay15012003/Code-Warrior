import random

from hangman_art import stages, logo
from hangman_random_words import word_list

lives = 6

print(logo)

random_word = random.choice(word_list)

random_word_len = len(random_word)

placeholder = ""
for letters in random_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    user_guess = input("Enter a letter : ").lower()

    if user_guess in correct_letters:
        print(f"You have already guessed {user_guess}")

    build_word = ""

    for letter in random_word:
        if letter == user_guess:
            build_word += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            build_word += letter
        else:
            build_word += "_"

    print(build_word)

    if user_guess not in random_word:
        lives -= 1
        print()
        print(stages[lives])
        print(f"You have {lives} lives left")
        print()

        if lives == 0:
            game_over = True
            print(f"-----The correct word was {random_word}! You lose-----")

    if "_" not in build_word:
        game_over = True
        print()
        print("-----You Won-----")