from turtle import Turtle, Screen
#
# Constructing an object of Turtle and Screen class.
slow = Turtle()
show = Screen()

# Setting the shape of the slow object to turtle using the shape() method of the Turtle class.
slow.shape("turtle")
#
# Setting the color of the slow object to red4 using the shape() method of the Turtle class.
slow.fillcolor("red4")
#
# Setting the background color to black using bgcolor() method of the Screen class.
show.bgcolor("gray")
#
# Move the slow object forward by 100 spaces using the forward() method of the Turtle class.
slow.forward(100)
#
# Tapping into the exitonclick() method of the Screen class.
show.exitonclick()

# Installed "prettytable" package from the PyPI.
# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# # Adding columns the table object.
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# # Printing the table.
# print(table)
