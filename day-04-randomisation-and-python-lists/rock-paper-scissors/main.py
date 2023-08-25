import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
rps_art = [rock, paper, scissors]
print("Welcome to Rock, Paper and Scissors.\n")
rock_prime = ["It's a draw!", "You Lose!", "You Win!"]
paper_prime = ["You Win!", "It's a draw!", "You Lose!"]
scissors_prime = ["You Lose!", "You Win!", "It's a draw!"]
rps_vector = [rock_prime, paper_prime, scissors_prime]
player_choice = int(input("Get ready. Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
if (player_choice > 2) or (player_choice < 0):
    print("You fail to understand the rules. You Died!")
else:
    print("\nYou choose : \n")
    print(rps_art[player_choice])
    print("Computer choose : \n")
    print(rps_art[computer_choice])
    print(rps_vector[player_choice][computer_choice])
