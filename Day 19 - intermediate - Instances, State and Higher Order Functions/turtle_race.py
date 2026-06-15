from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

turtles = []
colors = ["red", "blue", "purple", "green", "yellow", "orange"]
y_positions = [-50,-30,-10,10,30,50]

def color_turtles():
    for i in range(6):
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[i])
        turtles.append(new_turtle)

def turtles_penup():
    for turtle in turtles:
        turtle.penup()

def race_startup():
    turtles_penup()
    for i in range (6):
        turtles[i].goto(-230,y_positions[i])

def race_begins():
    winning_turtle = ""
    while not winning_turtle:
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            if turtle.xcor() >= 230:
                winning_turtle = turtle.pencolor()
    return winning_turtle



color_turtles()
race_startup()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
winner = race_begins()
if winner == user_bet.lower():
    print (f"You guessed {user_bet}.\nWinner is {winner}.\nYou win!")
else:
    print (f"You guessed {user_bet}.\nWinner is {winner}.\nYou lose!")


screen.exitonclick()