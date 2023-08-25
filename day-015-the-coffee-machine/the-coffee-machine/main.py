# Procedural Programming.
from menu import MENU, resources


def get_coins():
    """Calculates the number of coins (quarters, dimes, nickels and pennies). Returns the total cost of the coffee in
    dollars"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return total


def get_resources(coffee_choice):
    """Deducts resources from the Coffee Machine inventory."""
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    if coffee_choice == "latte" or coffee_choice == "cappuccino":
        resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]


def check_resources(coffee_choice):
    """Checks if we have enough resources in the Coffee Machine inventory. Returns 'off' if we don't have enough."""
    if MENU[coffee_choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return "off"
    elif MENU[coffee_choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough water.")
        return "off"
    if coffee_choice == "latte" or coffee_choice == "cappuccino":
        if MENU[coffee_choice]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return "off"


def coffee_machine():
    prompt = ""
    money = 0
    while prompt != 'off':
        prompt = input("What would you like? (espresso/latte/cappuccino) :").lower()
        if prompt == 'report':
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif prompt == 'off':
            continue
        elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
            if check_resources(prompt) == "off":
                continue
            total_coins = get_coins()
            cost = MENU[prompt]["cost"]
            if total_coins > cost:
                get_resources(prompt)
                money += cost
                print(f"Here is ${round(total_coins - cost, 2)} in change.")
                print(f"Here is your {prompt} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"There is no {prompt} in the Menu.")


coffee_machine()
