import random
from hangman_words import word_list

keep_playing = input("Do you want to Play? (yes/no) ").lower() # asking if player wants to play

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

while keep_playing == "yes": # loop for play and keep playing

    chosen_word = random.choice(word_list) # select a word from the word list

    placeholder = "" #creating a place holder

    word_length = len(chosen_word) # word lenght

    for position in range(0,word_length): # now that we know the word, adding the ___ for each letter in word to the place holder
        placeholder += "_"
    print(placeholder)


    game_over = False # setting game over as false
    correct_letters =[] # creating an empty list for the correct letters
    lives = 6 # setting the number of lives



    while not game_over:   # this loop is to run until the game is not over
        print(f"************************<{lives} LIVES LEFT>************************") # display to the user the number of remaining lives
        guess = input("Please guess a letter: ").lower() # asking the user to input a word

        if len(guess) != 1 or not guess.isalpha(): # this if statement is to ensure that the user do not typer more than one letter
            print("Please enter a single letter.")
            continue # if the message above it goes back to the start of the loop

        if guess in correct_letters:
            print(f"You already guessed {guess}") # check and tell the user if the letter was already used

        display = "" #creating the display

        for letter in chosen_word:       #this loop will add the letter to the display for each correct guess and replace the _
            if letter == guess:
                display += letter
                if guess not in correct_letters:
                    correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)

        if guess not in chosen_word:  #this loop reduces the number of lives and tell the user that the chosen letter is wrong
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0: # sets the game over in case the user makes the 6 mistakes
            game_over = True
            print("You lose.")
            print(f"The word was {chosen_word}")

        if "_" not in display: # the game is over when there are no _ remaning in display and tells the user that he won the game
            game_over = True
            print("You win!")

        print(hangman_stages[6 - lives]) # prints the hangman stages
    keep_playing = input("Do you want to play again? (yes/no): ").lower() # when game is over (winning or losing), it asks the user if he wants to keep playing 
