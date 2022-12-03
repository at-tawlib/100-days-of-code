from turtle import Turtle

# tuple to hold positions to make the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []  # to hold snake body
        self.create_snake()

    def create_snake(self):
        """Create the snake body using 3 turtle objects
        each turtle has a size of 20"""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """move last segment to second to last segment; and so on
          i.e. get segment before last segment position and set it to the last segment
          this goes until the first segment"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # then move the first segment
