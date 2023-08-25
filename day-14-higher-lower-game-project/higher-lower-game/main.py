from art import logo, vs
from game_data import data
import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')


choice = {'A': random.choice(data),
          'B': random.choice(data)
          }

if choice['A'] == choice['B']:
    choice['B'] = random.choice(data)


def higher_lower():
    my_score = 0
    to_continue = True
    while to_continue:
        clear()
        print(logo)
        if my_score > 0:
            print(f"You're right! Current score: {my_score}.")
        print(f"Compare A: {choice['A']['name']}, a {choice['A']['description']}, from {choice['A']['country']}.")
        print(vs)
        print(f"Against B: {choice['B']['name']}, a {choice['B']['description']}, from {choice['B']['country']}.")
        my_choice = input("Who has more followers? Type 'A' or 'B':").upper()
        if my_choice == 'A' and choice['A']['follower_count'] > choice['B']['follower_count']:
            my_score += 1
        elif my_choice == 'B' and choice['B']['follower_count'] > choice['A']['follower_count']:
            my_score += 1
            choice['A'] = choice['B']
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {my_score}")
            return
        choice['B'] = random.choice(data)


higher_lower()
