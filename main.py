import os
from art import logo, vs
from game_data import data
from random import randint

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0
right = True

while right:
    random_a = randint(0, len(data) - 1)
    random_b = randint(0, len(data) - 1)

    if random_a == random_b:
        random_b = randint(0, len(data) - 1)

    a = data[random_a]
    b = data[random_b]

    if a["follower_count"] > b["follower_count"]:
        higher = a
    elif b["follower_count"] > a["follower_count"]:
        higher = b

    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    cls()

    if  choice == 'A' and higher == a:
        score += 1
    elif choice == 'A' and higher == b:
        right = False
        print(f"Sorry, that's wrong. Final score: {score}")
    elif choice == 'B' and higher == a:
        right = False
        print(f"Sorry, that's wrong. Final score: {score}")
    elif choice == 'B' and higher == b:
        score += 1