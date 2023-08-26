# Opens file.txt.
# file = open("file.txt")

# Reads the contents of the file using the read() function and stores its contents as a string in a variable named
# 'contents'. contents = file.read()

# Prints the content of the 'contents' variable.
# print(contents)

# Closes file.txt.
# file.close()

# OR

# Using the with keyword, I no longer have to close the file manually.
# Once the indented block within 'with' is executed the file will close automatically.
# with open("file.txt") as file:
#      contents = file.read()

# with open("file.txt", mode="a") as file:
#     file.write("\nHey, Meowya.")
#
#
# with open("file.txt") as file:
#     contents = file.read()
#     print(contents)

# Absolute File Path.
# with open("C:/Users/Meowya/PycharmProjects/data/day_024_data.txt", mode="a") as file:
#     file.write("\nHey, Meowya.")

# with open("C:/Users/Meowya/PycharmProjects/data/day_024_data.txt") as file:
#     contents = file.read()
#     print(contents)

# Relative File Path
with open("../data/day_024_data.txt") as file:
    contents = file.read()
    print(contents)
