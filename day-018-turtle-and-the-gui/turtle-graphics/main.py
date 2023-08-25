from turtle import Turtle, Screen
from random import randint, choice

my_turtle = Turtle()
# my_turtle.shape("turtle")

my_screen = Screen()
my_screen.colormode(255)


# Challenge 1 - Draws a square of size 100.
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# Challenge 2 - Draw a dashed line.
# for _ in range(5):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# Challenge 3 - Drawing different shapes.
# def draw_shape(shape_sides, shape_angles):
#     my_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(shape_sides):
#         my_turtle.forward(100)
#         my_turtle.right(shape_angles)
#
#
# for each_shape in range(3, 11):
#     draw_shape(each_shape, 360 / each_shape)

# Challenge 4 - Generate a Random Walk.
# my_turtle.speed(10)
# my_turtle.pensize(10)
# random_walk = [0, 90, 180, 270]
# for _ in range(100):
#     # (randint(0, 255), randint(0, 255), randint(0, 255)) is a tuple.
#     my_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     my_turtle.forward(20)
#     # my_turtle.right(choice(random_walk))
#     # OR
#     my_turtle.setheading(choice(random_walk))

# Challenge 5 - Draw a Spirograph
my_turtle.speed(0)
for tilt in range(0, 360, 4):
    my_turtle.setheading(tilt)
    my_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    my_turtle.circle(100)

my_screen.exitonclick()
