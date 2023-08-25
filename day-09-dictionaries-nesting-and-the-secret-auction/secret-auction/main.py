from art import logo
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')


# HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the Secret Auction.")
end_of_auction = False
max_bid = 0
max_bidder = ""
blind_auction = {}
while not end_of_auction:
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What's your bid? $: "))
    bidder_choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    blind_auction[bidder_name] = bidder_price
    if bidder_choice == 'yes':
        clear()
    elif bidder_choice == 'no':
        end_of_auction = True
    else:
        print("Invalid choice.")
        end_of_auction = True

for bidder in blind_auction:
    if blind_auction[bidder] > max_bid:
        max_bid = blind_auction[bidder]
        max_bidder = bidder
clear()
print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
