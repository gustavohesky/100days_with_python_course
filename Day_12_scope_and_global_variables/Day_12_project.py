
'''Guessing game'''


'''

User needs to input a number
check if number is higher or lower or equal to the chosen number
return an answer
if lower or higher -> deduct one life
easy mode = 10 guesses
hard mode = 5 guesses

When lives = 0, game over

'''

import random

chosen_number = random.choice(range(1,101))

mode = {"easy":10,"hard":5}

user_mode = input("Please choose dificulty (easy/hard): ").lower()

if user_mode not in mode:
    print("Please select a valid option (easy/hard) ")
    exit()

lives = mode[user_mode]

print(chosen_number)

def check_number(user_guess,chosen_number,lives):
    if user_guess > chosen_number:
        print("Too high")
        return lives -1
    elif user_guess < chosen_number:
        print("Too low")
        return lives -1
    else:
        print("You won!")
        return lives

while lives > 0:
    print(f"You have {lives} lives remaining.")
    user_guess = int(input("What is your guess?\nPlease choose a number between 1 and 100: "))
    
    lives = check_number(user_guess, chosen_number, lives)

    if user_guess == chosen_number:
        break



if lives == 0 and user_guess != chosen_number:
    print("Game Over! You ran out of lives.")
    print(f"The number was {chosen_number}")
