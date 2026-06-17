from mimetypes import init
from turtle import Turtle

class Paddle (Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.left(90)
        self.shapesize(stretch_len=5)
        self.teleport(cords[0], cords[1])

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)







