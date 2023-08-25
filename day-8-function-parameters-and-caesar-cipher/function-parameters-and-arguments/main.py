# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet(my_name):
#     print(f"Hi, {my_name}!")
#     print(f"Hey, {my_name}!")
#     print(f"Hello There, {my_name}!")

# greet("K")
# Functions with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}.")


# Function call with Positional arguments
# greet_with("Meowya", "Thundera")

# Function call with Keyword arguments
greet_with(location="Thundera", name="Meowya")


