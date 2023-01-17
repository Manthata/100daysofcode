import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.listen()

player = Player()
carmanager = CarManager()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if player.check_finish():
        player.reset()
        carmanager.increment_speed()

    
    carmanager.make_car()
    carmanager.move()
    screen.update()

    for car in carmanager.cars:
        if car.distance(player) <= 20:
            game_is_on = False
            # Icreament the speed


    
screen.exitonclick()