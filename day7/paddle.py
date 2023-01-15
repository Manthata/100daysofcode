from turtle import Turtle


INITIAL_POSITION = (-300,0)
DISTANCE = 100 # pixels the snake will move each time



class Paddle(Turtle):
    """_summary_
    """
    def __init__(self, initial_position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.move_speed = 0.1
        self.goto(initial_position)

    
    def move_up(self):
        """
        Hi
        """
        new_y = self.ycor() + 80
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        """
        Hello
        """
        new_y = self.ycor() - 80
        self.goto(self.xcor(), new_y)


    


