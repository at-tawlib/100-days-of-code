# day 18 draw a spirograph using turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    """generates a random colour"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    """takes size of a gap,uses it to determine the number of times to draw the circle"""
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim.speed("fastest")

draw_spirograph(2)
tim.penup()
tim.setposition(200, 200)
tim.pendown()

draw_spirograph(10)
tim.penup()
tim.setposition(-300, -200)
tim.pendown()

draw_spirograph(20)
tim.penup()
tim.setposition(-300, 300)
tim.pendown()

draw_spirograph(50)
tim.penup()
tim.setposition(300, -300)
tim.pendown()

draw_spirograph(35)

screen = t.Screen()
screen.exitonclick()
