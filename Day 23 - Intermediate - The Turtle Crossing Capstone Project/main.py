import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

tick = 1
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    if tick == 6:
        car_manager.spawn_car()
        tick = 1
    car_manager.cars_move()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > player.f_line:
        player.restart_pos()
        scoreboard.increase_level()
        car_manager.increase_speed()

    time.sleep(0.1)
    tick += 1
    screen.update()

screen.exitonclick()
