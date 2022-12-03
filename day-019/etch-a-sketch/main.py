# Day -19
# create a turtle to draw on the screen
# use w = forward, s = backward, a = counter clockwise, d = clockwise and c = clear

from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_clockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_anticlockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(move_clockwise, "d")
screen.onkey(move_anticlockwise, "a")
screen.onkey(clear, "c")
screen.exitonclick()

