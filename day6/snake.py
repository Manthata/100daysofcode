





from ast import Not
from turtle import Turtle

INITIAL_POSITION = [(0,0), (-20,0), (-40, 0)]
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
class Snake:
    """
    snake class
    """

    def __init__(self) -> None:
        """
        Initialize the snake object
        """
        self.segments = []
        self.make_body()
        self.head = self.segments[0]
        self.direction = 0
        pass

    def make_body(self):
        """
        This function should move the snake
        """
        
        for position in INITIAL_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        """Move the snake"""

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
    
    def turn_left(self):
        """Turn left"""
        if self.direction != RIGHT:
            self.head.setheading(LEFT)
            self.direction = LEFT
    
    def turn_right(self):
        """Turn right"""
        if self.direction != LEFT:
            self.head.setheading(RIGHT)
            self.direction = RIGHT
    
    def turn_up(self):
        """Turn up"""
        if self.direction != DOWN:
            self.head.setheading(UP)
            self.direction = UP
    def turn_down(self):
        """Turn down"""
        if self.direction != UP:
            self.head.setheading(DOWN)
            self.direction = DOWN



