import turtle
import pandas

# create screen with image as background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get data from the .csv file
data = pandas.read_csv("50_states.csv")
# get states into a list
all_states = data.state.to_list()
guessed_states = []  # stores guessed states

while len(guessed_states) < 50:
    # get answer from input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?d").title()
    if answer_state == "Exit":
        # export the remaining states to states_to_learn.csv
        missing_states = [state for state in all_states if state not in guessed_states]

        # create dataframe
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    # if answer_state is one of the states in all the states of the 50_states.csv
    #   create a turtle to write the name of the state at the state's coordinates
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
