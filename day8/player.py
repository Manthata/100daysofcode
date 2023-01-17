from turtle import Turtle



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """


    Args:
        Turtle (_type_): _description_
    """

    def __init__(self) -> None:
        super().__init__()

        self.move_y = 10
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """
        moves the player across the screen 
        """
        new_y = self.ycor() + self.move_y
        new_x = self.xcor()
        self.goto(new_x,new_y)
    

    def check_finish(self):
        """_summary_
        """
        if self.ycor() >= FINISH_LINE_Y:
            return True
    
    def reset(self):
        """_summary_
        """
        self.goto(STARTING_POSITION)
    





