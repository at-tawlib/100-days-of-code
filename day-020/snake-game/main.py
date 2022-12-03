# Day 20 - Snake Project
from turtle import Turtle, Screen
import time

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)     # cancel animation

# tuple to hold positions to make the snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []  # to hold snake body

# Create the snake body using 3 turtle objects
# each turtle has a size of 20
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # update screen after action has occurred
    time.sleep(0.1)
    """move last segment to second to last segment; and so on
    i.e. get segment before last segment position and set it to the last segment
    this goes until the first segment"""
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)    # then move the first segment






screen.exitonclick()
