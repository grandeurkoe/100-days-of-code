# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from os import system, name
from art import logo
import random


def clear():
    if name == 'nt':
        _ = system('cls')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def who_won(my_cards, dealer_cards, dealer_first_card):
    print(f"Your final hand : {my_cards}, Final score : {sum(my_cards)}")
    dealer_cards.append(dealer_first_card)
    dealer_cards.append(random.choice(cards))
    while sum(dealer_cards) < 17 and sum(dealer_cards) < sum(my_cards):
        dealer_cards.append(random.choice(cards))
    print(f"Computer's final hand : {dealer_cards}, Final score : {sum(dealer_cards)}")
    if sum(my_cards) == 21:
        print("You have a Blackjack. You Won.")
    elif sum(dealer_cards) == 21:
        print("Computer has a Blackjack. You Lose.")
    elif sum(my_cards) == sum(dealer_cards):
        print("It's a draw.")
    elif sum(my_cards) > 21 and 11 in my_cards:
        my_cards[my_cards.index(11)] = 1
        if sum(dealer_cards) < sum(my_cards) < 21:
            print("You Win.")
        else:
            print("You went over. You Lose")
    elif sum(my_cards) > 21:
        print("You went over. You Lose.")
    elif sum(dealer_cards) > 21 and 11 in dealer_cards:
        dealer_cards[dealer_cards.index(11)] = 1
        if sum(my_cards) < sum(dealer_cards) < 21:
            print("You Win.")
        else:
            print("You went over. You Lose.")
    elif sum(dealer_cards) > 21:
        print("Computer went over. You Win.")
    elif sum(my_cards) == 21 and sum(dealer_cards) == 21:
        print("It's a draw.")
    elif sum(dealer_cards) < sum(my_cards) < 21:
        print("You Won.")
    elif sum(my_cards) < sum(dealer_cards) < 21:
        print("You Lose.")
    else:
        print("You Lose.")
    blackjack()


def blackjack():
    start_game = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no : ").lower()
    if start_game == 'y':
        clear()
        print(logo)
        your_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = []
        computer_first_card = random.choice(cards)
        not_passing = True
        while not_passing:
            print(f"Your cards : {your_cards}, Current score : {sum(your_cards)}")
            print(f"Computer's first card : {computer_first_card}")
            if sum(your_cards) >= 21:
                who_won(your_cards, computer_cards, computer_first_card)
            to_pass = input("Type 'y' to get another card, type 'n' to pass : ").lower()
            if to_pass == 'n':
                who_won(your_cards, computer_cards, computer_first_card)
                not_passing = False
            elif to_pass == 'y':
                your_cards.append(random.choice(cards))
    else:
        quit()


blackjack()
