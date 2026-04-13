import random
from hangman_words import word_list

keep_playing = input("Do you want to Play? (yes/no) ").lower()

hangman_stages = [
# Stage 0
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
# Stage 1
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
# Stage 2
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
# Stage 3
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
# Stage 4
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
# Stage 5 (final)
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
# Stage 6 (game over)
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

while keep_playing == "yes":

    chosen_word = random.choice(word_list)

    placeholder = ""

    word_length = len(chosen_word)

    for position in range(0,word_length):
        placeholder += "_"
    print(placeholder)


    game_over = False
    correct_letters =[]
    lives = 6



    while not game_over:
        print(f"************************<{lives} LIVES LEFT>************************")
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in correct_letters:
            print(f"You already guessed {guess}")

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                if guess not in correct_letters:
                    correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The word was {chosen_word}")

        if "_" not in display:
            game_over = True
            print("You win!")

        print(hangman_stages[6 - lives])
    keep_playing = input("Do you want to play again? (yes/no): ").lower()
