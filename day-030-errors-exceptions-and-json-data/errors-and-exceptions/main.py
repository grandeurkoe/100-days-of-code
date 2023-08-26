# Day 30 - Errors, Exceptions and JSON Data

# FileNotFoundError
# with open("trial_file.txt", mode="r") as file:
#     file.read()

# KeyError
# my_dict = {"key": "value"}
# print(my_dict["doesn't exist"])

# IndexError
# my_list = ["apple", "banana", "pear"]
# print(my_list[3])

# TypeError
# int_var = 50
# print("The int value is: " + int_var)

# Catching Exceptions

# try:
#     file = open("trial_file.txt")
#     my_dict = {"key": "value"}
#     # print(my_dict["doesn't exist"])
# except FileNotFoundError:
#     # print("Couldn't open \"trial_file.txt\".")
#     file = open("trial_file.txt", mode="w")
#     file.write("Writing in Exception block.")
# except KeyError as error_message:
#     # You can get the error message printed on the console during exceptions by using the 'as' keyword.
#     print(f"The key {error_message} doesn't exist.")
# else:
#     file_contents = file.read()
#     print(file_contents)
# finally:
#     file.close()
#     print("All file operations completed.")
#     print("File Closed.")

# Raising your own exceptions.

height = int(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height cannot be over 3 meters.")

BMI = weight / height ** 2
print(BMI)
