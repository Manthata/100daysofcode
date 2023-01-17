from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    """_summary_

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self) -> None:

        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
    
    def make_car(self):
        """_summary_
        """
        make_car = random.randint(1, 6)
        if make_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            color = random.choice(COLORS)
            new_car.color(color)
            new_position = random.randint(-250, 250)
            new_car.goto(300, new_position)
            self.cars.append(new_car)


    
    def move(self):
        """_summary_
        """
        for car in self.cars:
            car.backward(self.speed)
    
    def increment_speed(self):
        """_summary_
        """
        self.speed = self.speed + MOVE_INCREMENT

    
