# Calculator
from art import logo
from os import name, system


def clear():
    if name == 'nt':
        _ = system('cls')


# Add two numbers namely, number1 and number2
def add(number1, number2):
    return number1 + number2


# Subtract two numbers namely, number1 and number2
def subtract(number1, number2):
    return number1 - number2


# Multiply two numbers namely, number1 and number2
def multiply(number1, number2):
    return number1 * number2


# Divide two numbers namely, number1 and number2, as long as the denominator != 0
def divide(number1, number2):
    if number2 == 0:
        print("You can't divide by 0.")
    else:
        return number1 / number2


# Dictionary with all the mathematical operations.
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }


def calculator():
    to_continue = 'y'
    print(logo)
    number1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    while to_continue == 'y':
        what_operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        function_name = operations[what_operation]
        result = function_name(number1, number2)
        print(f"{number1} {what_operation} {number2} = {result}")

        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if to_continue == 'y':
            number1 = result
        else:
            clear()
            calculator()


calculator()
