import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []

def give_card(hand):
    hand.append(random.choice(cards))

def show_hands():
    print(f"Player: {player} | Total: {sum(player)}")
    print(f"Dealer: {dealer} | Total: {sum(dealer)}")
    print("-" * 30)

print(r"""
  ____  _            _        _            _    
 |  _ \| |          | |      | |          | |   
 | |_) | | __ _  ___| | __   | | __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <    | | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\   |_|\__,_|\___|_|\_\
                                                 
                 BLACKJACK GAME ♠️♥️♣️♦️
""")



play = input("Do you want to play blackjack (y/n)? ").lower()

if play == "y":

    give_card(player)
    give_card(player)

    give_card(dealer)
    give_card(dealer)

    show_hands()

    if sum(player) == 21:
        print("Blackjack! You win!")
    elif sum(dealer) == 21:
        print("Dealer has Blackjack! You lose!")
    else:


        keep_playing = True

        while keep_playing:
            choice = input("Do you want another card (y/n)? ").lower()

            if choice == "y":
                give_card(player)
                show_hands()

                if sum(player) > 21:
                    print("You went over 21. You lost!")
                    keep_playing = False

                elif sum(player) == 21:
                    print("You hit 21!")
                    keep_playing = False

            else:
                keep_playing = False


        if sum(player) <= 21:
            while sum(dealer) < 17:
                give_card(dealer)

            show_hands()


            if sum(dealer) > 21:
                print("Dealer busted. You win!")

            elif sum(player) > sum(dealer):
                print("You win!")

            elif sum(player) < sum(dealer):
                print("You lose!")

            else:
                print("It's a draw!")



