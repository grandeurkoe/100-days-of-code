from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()
my_turtle.speed(10)


def go_forward():
    """Moves my_turtle object forwards by 10 spaces."""
    my_turtle.forward(10)


def go_backward():
    """Moves my_turtle object backwards by 10 spaces."""
    my_turtle.backward(10)


def rotate_clockwise():
    """Rotate my_turtle clockwise by 10 degrees."""
    my_turtle.right(10)


def rotate_counterclockwise():
    """Rotate my_turtle clockwise by 10 degrees."""
    my_turtle.left(10)


def clear_screen():
    """Clears my_screen."""
    my_screen.resetscreen()


# Use the listen() function to listen for keystrokes.
my_screen.listen()

# On pressing "right" the onkey() function will move my_turtle to the right by 10 spaces.
# When passing a function as arguments, we do not include round braces.
my_screen.onkeypress(fun=go_forward, key="w")
my_screen.onkeypress(fun=go_backward, key="s")
my_screen.onkeypress(fun=rotate_clockwise, key="d")
my_screen.onkeypress(fun=rotate_counterclockwise, key="a")
my_screen.onkey(fun=clear_screen, key="c")

my_screen.exitonclick()
