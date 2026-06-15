from turtle import Turtle, Screen

nat = Turtle()
screen = Screen()

def move_forward():
    nat.forward(10)

def move_backward():
    nat.backward(10)

def turn_left():
    nat.left(10)

def turn_right():
    nat.right(10)

def up_down():
    if nat.isdown():
        nat.penup()
    else:
        nat.pendown()

def clear_reset():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear_reset)
screen.onkey(key="space", fun=up_down)
screen.exitonclick()