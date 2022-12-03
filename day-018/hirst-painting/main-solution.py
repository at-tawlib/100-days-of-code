# Solution to hirst painting question
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(241, 229, 79), (193, 10, 71), (208, 158, 97), (110, 179, 206), (163, 171, 33), (23, 118, 174), (162, 72, 35), (214, 137, 169), (30, 136, 73), (7, 35, 85), (234, 70, 40), (120, 182, 137), (239, 221, 4), (213, 83, 129), (80, 19, 80), (11, 58, 36), (238, 161, 190), (180, 44, 88), (10, 44, 127), (7, 102, 62), (120, 39, 23), (20, 168, 199), (6, 86, 97), (146, 208, 217), (161, 210, 186), (95, 38, 22)]

# move to bottom left of screen
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # move up after painting ten dots to start again
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
