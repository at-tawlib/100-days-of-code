# Day 20 - Snake Project
from turtle import Turtle, Screen
from snake import Snake
import time

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)     # cancel animation

snake = Snake()
screen.listen()
# move the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# while game is on, update screen every 0.1 seconds
while game_is_on:
    screen.update()  # update screen after action has occurred
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
