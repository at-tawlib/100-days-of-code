# Day 18 Project: Draw a hirst-painting
import turtle as tk
import random
# import colorgram
#
# rgb_colors = []
# # Extracts colors form an image
# colors = colorgram.extract("image.jpg", 30)
# # extract the rgb values and add to list
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# # print rgb tuples and copy it into a color_list
# print(rgb_colors)
color_list = [(241, 229, 79), (193, 10, 71), (208, 158, 97), (110, 179, 206), (163, 171, 33), (23, 118, 174), (162, 72, 35), (214, 137, 169), (30, 136, 73), (7, 35, 85), (234, 70, 40), (120, 182, 137), (239, 221, 4), (213, 83, 129), (80, 19, 80), (11, 58, 36), (238, 161, 190), (180, 44, 88), (10, 44, 127), (7, 102, 62), (120, 39, 23), (20, 168, 199), (6, 86, 97), (146, 208, 217), (161, 210, 186), (95, 38, 22)]

timmy = tk.Turtle()
tk.colormode(255)
screen = tk.Screen()
timmy.penup()
timmy.setx(-screen.canvwidth)
timmy.sety(-screen.canvheight)


def draw_horizontal():
    for i in range(10):
        timmy.color(random.choice(color_list))
        timmy.pendown()
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)


for _ in range(5):
    draw_horizontal()
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)

    draw_horizontal()
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)


screen.exitonclick()
