import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# instance of a new object
new_turtle = turtle.Turtle()
new_turtle.hideturtle()

# read csv with Pandas
location = pd.read_csv("50_states.csv")

def setposition(x, y, state):
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.write(state)

def settitle(title):
    return screen.textinput(title=title, prompt="Type another state's name:")

# control game score
score = 0
# start title
title_new="Type a State"
# control the states to avoid to count more than one time
control_state = []
# full names of states is a listAe
full_state_list = location["state"].to_list()
# pop-up start a text box
# answer_state = screen.textinput(title=title_new, prompt="Type another state's name:")

while score < 50:
    # pop-up start a text box
    state_type = settitle(title_new).upper()

    # help to show all the States
    if state_type == 'HELP':
        # iterate with all values in state column (series)
        for index, value in location["state"].items():
            check = str(value).upper()
            state_value = location[location["state"].str.upper() == check]
            setposition(int(state_value['x']), int(state_value['y']), state_value["state"].item())
    if state_type == 'EXIT':
        break

    state_value = location[location["state"].str.upper() == state_type]

    if len(state_value) > 0 and state_value["state"].item() not in control_state:
        score += 1
        setposition(int(state_value['x']), int(state_value['y']), state_value["state"].item())
        control_state.append(state_value["state"].item())
        title_new = f"{score} of 50"

    if score == 0:
        title_new = 0

# consolidate the list and keep a list for what the user didn't guess
consolation_list = []
for n in  full_state_list:
    if n not in control_state:
        consolation_list.append(n)

data_missed = {"states you missed": consolation_list}
dataframe = pd.DataFrame(data=data_missed)

dataframe.to_csv("to_learn.csv")

turtle.exitonclick()

# get coordination from any image
# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
