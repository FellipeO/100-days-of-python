from turtle import Turtle

X_CORDS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_block = Turtle("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(X_CORDS[i], 0)
            self.segments.append(new_block)

    def add_segment(self):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(self.segments[-1].pos())
        self.segments.append(new_block)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
