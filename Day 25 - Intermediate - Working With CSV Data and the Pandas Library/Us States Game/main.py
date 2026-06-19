import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
hits = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{hits}/50 Guess the state", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    for state in data["state"]:
        if answer_state == state and answer_state not in correct_guesses:
            my_turtle.goto(data.loc[data["state"] == state, "x"].item(), data.loc[data["state"] == state, "y"].item())
            my_turtle.write(answer_state, align="center")
            correct_guesses.append(answer_state)
            hits += 1

states_to_learn = [state for state in data.state if state not in correct_guesses]
df = pd.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
