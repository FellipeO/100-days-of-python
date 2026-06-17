import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def spawn_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2)
        new_car.penup()
        new_car.right(180)
        new_car.color(random.choice(COLORS))
        new_car.goto(300,random.randint(-250,250))
        self.cars.append(new_car)

    def cars_move(self):
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -280:
                car.hideturtle()
                self.cars.remove(car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
