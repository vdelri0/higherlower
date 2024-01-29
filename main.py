import os
from art import logo, vs
from game_data import data
from random import choice


score = 0
should_continue = True

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
    """Format the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the users guess and follower count and returns if they got It right."""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

while should_continue:
    a = choice(data)
    b = choice(data)

    while a == b:
        b = choice(data)

    print(logo)
    print(f"Compare A: {format_data(a)}.")
    print(vs)
    print(f"Against B: {format_data(b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    cls()

    a_follower_count = a["follower_count"]
    b_follower_count = b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
