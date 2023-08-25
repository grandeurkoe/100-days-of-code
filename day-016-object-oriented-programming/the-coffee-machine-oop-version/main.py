from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
resources = CoffeeMaker()
money = MoneyMachine()

is_true = True
while is_true:
    prompt = input(f"What would you like? ({coffee_menu.get_items()[:-1]}): ").lower()
    if prompt == "report":
        resources.report()
        money.report()
    elif prompt == "off":
        is_true = False
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        my_coffee = coffee_menu.find_drink(prompt)
        if resources.is_resource_sufficient(my_coffee):
            if money.make_payment(my_coffee.cost):
                resources.make_coffee(my_coffee)

    else:
        print(f"There is no {prompt} in the Menu.")
