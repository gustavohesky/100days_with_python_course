import random
import celebrities as c



def get_random_person():
    return random.choice(c.celebrities)

def display_round(person_a,person_b):
    print(f"{person_a['name']} - {person_a['description']}")
    print("VS")
    print(f"{person_b['name']} - {person_b['description']}\n")

def get_choice(person_a,person_b):
    return input(f"Who has more followers? A:{person_a['name']} or B:{person_b['name']} ?").lower()

def check_answer(choice, person_a,person_b):
    if choice == 'a':
        return person_a["followers"] > person_b["followers"]
    if choice == 'b':
        return person_b["followers"] > person_a["followers"]
    else:
        return False
    

def game():
    score = 0
    game_over = False

    person_a = get_random_person()
    person_b = get_random_person()

    while person_a == person_b:
        person_b = get_random_person()
    
    while not game_over:
        display_round(person_a,person_b)
        choice = get_choice(person_a,person_b)
        is_correct = check_answer(choice,person_a,person_b)

        if is_correct:
            score +=1
            print(f"\nCorrect! Score: {score}")
            if choice == "b":
                person_a = person_b

            person_b = get_random_person()

            # avoid duplicates
            while person_a == person_b:
                person_b = get_random_person()

        else:
            print("\nGame Over")
            print(f"Final score: {score}")
            game_over = True


game()