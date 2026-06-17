from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.off_y = 0.1
        self.off_x = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.off_x
        new_y = self.ycor() + self.off_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.off_y *= -1

    def bounce_x(self):
        self.off_x *= -1.1

    def reset_ball(self):
        self.off_x *= -1
        self.off_y *= -1
        self.home()

    def reset_speed(self):
        self.off_y = 0.1
        self.off_x = 0.1
