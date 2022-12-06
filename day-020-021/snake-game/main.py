# Day 20 - Snake Project
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)     # cancel animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()