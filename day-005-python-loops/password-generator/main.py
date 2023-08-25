# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for letter in range(1, nr_letters + 1):
#   password += random.choice(letters)
# for symbol in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
# for number in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
# print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# It only works if the password length is  less than or equal to 50.
# Improved code using while loop.
password = ""
letter_count = 0
symbol_count = 0
number_count = 0
count = 0
password_length = nr_letters + nr_symbols + nr_numbers
while count < password_length:
    rand_choice = random.randint(0, 2)
    if rand_choice == 0 and letter_count <= nr_letters - 1:
        password += random.choice(letters)
        letter_count += 1
    elif rand_choice == 1 and symbol_count <= nr_symbols - 1:
        password += random.choice(symbols)
        symbol_count += 1
    elif rand_choice == 2 and number_count <= nr_numbers - 1:
        password += random.choice(numbers)
        number_count += 1
    count = letter_count + symbol_count + number_count
print(password)

# password = []
# pass_word = ""
# for letter in range(1, nr_letters + 1):
#   password.append(random.choice(letters))
# for symbol in range(1, nr_symbols + 1):
#   password.append(random.choice(symbols))
# for number in range(1, nr_numbers + 1):
#   password.append(random.choice(numbers))
# random.shuffle(password)
# for pass_store in password:
#   pass_word += pass_store
# print(pass_word)
