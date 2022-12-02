# Day 018 (02-12-2022)
# Turtle & The Graphical User Interface (GUI)
import random
from turtle import Turtle, Screen
# create turtle
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


def reset_timmy(x_position, y_position):
    """clears screen and resets timmy position"""
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x_position, y_position)
    timmy_the_turtle.pendown()


reset_timmy(-250, 250)
# ################################## DRAW SQUARE ###############################
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# reset turtle position
reset_timmy(100, 100)

# # ################################## DRAW DASHED LINES ###############################
for i in range(20):
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)


# # ############################### DRAW SEQUENTIAL SHAPES ###############################
def draw_shape(num_sides):
    """Takes sides to draw a new shape"""
    angle = 360 / num_sides
    for shape in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", 'wheat', "SlateGrey", "SeaGreen"]
reset_timmy(0, 0)   # reset timmy
for shape_side in range(3, 11):
    timmy_the_turtle.color(random.choice(colours))
    draw_shape(shape_side)

# ###############################CREATE RANDOM WALK ##################################33
timmy_the_turtle.reset()
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fast")
directions = [0, 90, 180, 270]

for c in range(200):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
