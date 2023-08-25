from art import logo
import random

correct_guess = random.randint(1, 100)


def get_guesses(difficulty_level):
    """Returns the number of guess based on the difficulty option selected."""
    guess = 0
    if difficulty_level == 'easy':
        guess = 10
    elif difficulty_level == 'hard':
        guess = 5
    else:
        print(" Invalid difficulty selected.")

    return guess


def check_guess(player_number, guess_counter):
    """Checks if the player guessed the correct number."""
    if player_number == correct_guess:
        print(f"Good job! The correct guess is {player_number}.")
        guess_counter = -1
    elif player_number > correct_guess:
        print(f"{player_number} is too high.")
        guess_counter -= 1
    elif player_number < correct_guess:
        print(f"{player_number} is too low.")
        guess_counter -= 1

    return guess_counter


# Logo for the Number Guessing Game.
print(logo)
number_of_guesses = 0
print("Welcome to the Game of Number Guessing!")
print("Okay. Let me think of a number between 1 and 100.")

# For convenience let's print out the correct guess.
print(f"Pssst, the correct guess is {correct_guess}")

difficulty_option = input("Choose a difficulty option. Type 'easy' if you're a beginner and type 'hard' if you're an "
                          "experienced player : ")

number_of_guesses = get_guesses(difficulty_option)

while number_of_guesses > 0:
    print(f"Player has {number_of_guesses} attempts remaining to guess the correct number.")
    player_guess = int(input("What is your guess? "))
    number_of_guesses = check_guess(player_guess, number_of_guesses)
    if number_of_guesses > 0:
        print("Guess again.")
    elif number_of_guesses == 0:
        print("Player has run out of guesses. Player has lost the game.")
