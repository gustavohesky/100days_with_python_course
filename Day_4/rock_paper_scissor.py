# Rock, Paper, Scissor Game challange


import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


keep_playing = input("Do you want to play? (yes/no)")

while keep_playing == "yes":
    options = ["scissors","paper","rock"]

    player = input("Choose rock, paper or scissors: ").lower()
    if player not in options:
        print("Invalid choice!")

    computer = random.choice(options)

    if player == "rock":
        print(f"Player chose: {rock}")
    elif player == "paper":
        print(f"Player chose: {paper}")
    else:
        print(f"Player chose: {scissors}")

    if computer == "rock":
        print(f"Computer chose: {rock}")
    elif computer == "paper":
        print(f"Computer chose: {paper}")
    else:
        print(f"Computer chose: {scissors}")

    if player == "rock" and computer == "rock":
        print("Draw!")
    elif player == "rock" and computer == "paper":
        print("You Lost!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "paper":
        print("Draw!")
    elif player == "paper" and computer == "scissors":
        print("You Lost!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "scissors":
        print("Draw!")
    elif player == "scissors" and computer == "rock":
        print("You Lost!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    keep_playing = input("Do you want to keep playing? (yes/no)")