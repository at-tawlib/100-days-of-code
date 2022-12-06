from turtle import Turtle
# tuple to hold positions to make the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """create a turtle object with the following attributes"""
        self.segments = []  # to hold snake body
        self.create_snake()
        self.head = self.segments[0]    # set head of snake

    def create_snake(self):
        """Create the snake body with 3 segments each with a size of 20"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds a new segment to the snake segments"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """add a new segment to the snake"""
        # get the position of the last segment and adds new segment to it
        self.add_segment(self.segments[-1].position())

    def move(self):
        """move last segment to second to last segment; and so on
          i.e. get segment before last segment position and set it to the last segment
          this goes until the first segment"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # then move the first segment

    def up(self):
        """move up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """move down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """move left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """move right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
