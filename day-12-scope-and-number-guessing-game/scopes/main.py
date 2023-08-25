# Scope

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope - potion_strength is only accessible within the drink_potion function.

# def drink_potion() :
#     potion_strength = 2
#     print(potion_strength

# drink_potion()

# Global Scope - potion_health is accessible throughout the program.

# player_health = 10

# def drink_potion() :
#     potion_strength = 2
#     print(player_health)

# drink_potion()

# Modifying a Global Scope
# Avoid modifying a global variable within a local function.

# player_health = 10

# def drink_potion() :
#     global player_health
#     potion_strength = 2
#     player_health += potion_strength
#     print(player_health)

# drink_potion()

# Global Constants

PI = 3.14159
