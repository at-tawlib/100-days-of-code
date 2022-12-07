from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        """move turtle upwards when user presses up"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """move player to start position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """return True if car is at finish line else False"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
