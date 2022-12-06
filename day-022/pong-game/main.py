from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    # off animation

# create paddle on the right
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# listen to screen events
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# update screen
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
