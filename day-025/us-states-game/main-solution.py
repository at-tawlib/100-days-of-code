# day-025 [10-13-2022]
import turtle
import pandas
# Create a screen
screen = turtle.Screen()
screen.title("U.S. States Game")
# get image and set the turtle as the image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coord(x, y):
    """get coordinates of mouse clicked"""
    print(x, y)


# use 50_states.csv to check the correct answer and point it out on the screen
turtle.onscreenclick(get_mouse_click_coord)

# get states from the 50_states.csv file
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
x_coords = data.x.to_list()
y_coords = list(data.y)
data_dict = {}
for num in range(0, len(states_list)):
    data_dict[states_list[num]] = (x_coords[num], y_coords[num])

# get answer from player
cont_game = True
while cont_game:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?r")
    if answer_state.title() in data_dict:
        print("correct")
        new_turtle = turtle.Turtle("circle")
        new_turtle.penup()
        new_turtle.goto(data_dict[answer_state.title()])
        new_turtle.write(answer_state.title())
    else:
        print("wrong answer")





screen.exitonclick()
