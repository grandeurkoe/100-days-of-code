print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional
# .drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
left_or_right = input("You're at a cross road. Where do you want to go? " + 'Type "left" or "right" \n')
left_or_right = left_or_right.lower()
if left_or_right == "left":
    wait_or_swim = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type '
        '"swim" to swim across. \n')
    wait_or_swim = wait_or_swim.lower()
    if wait_or_swim == "wait":
        choose_ryb = input(
            "You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. "
            "Which color do you choose? \n")
        choose_ryb = choose_ryb.lower()
        if choose_ryb == "red":
            print("You enter a room engulfed in fire. Game Over.")
        elif choose_ryb == "yellow":
            print("It's a safe room. You Win!")
        elif choose_ryb == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You die unexpectedly. Game Over.")
    else:
        print("You were ambushed by trouts. Game Over.")
else:
    print("You fell into a hole. Game Over.")
