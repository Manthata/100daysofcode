from turtle import Turtle




DISTANCE = 20
INITIAL_ANGLE = 60

class Ball(Turtle):
    """_summary_

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 20
        self.move_y = 20
        self.ball_move = False
        self.move_speed = 0.1

    
    def stop(self):
        """
        Stops the ball from moving
        """
        self.ball_move = False
    
    def start(self):
        """
        Checks wheather it is okay to move and when it is okya it starts moving
        """
        self.ball_move = True
   
    def move(self):
        """
        Function responsible for moving the ball 

        """
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        bounces the ball in opposite y direction
        """
        self.move_y *=-1
        self.move_speed = self.move_speed * 0.9
    
    def bounce_x(self):
        """
        Bounce in the x direction
        """

        self.move_x *=-1
        self.move_speed = self.move_speed*0.9

    
    def reset(self):
        """_summary_

        """
        self.goto(0,0)
        self.stop()
        self.move_speed = 0.1




    
  



        