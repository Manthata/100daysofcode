
from turtle import Turtle



class ScoreBoard(Turtle):
    """_summary_

    Args:
        Turtle (_type_): Turtle class
    """

    def __init__(self) -> None:
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_score()
    

    def update_score(self):
        """_summary_
        """
        self.clear()
        self.goto(-100,200)
        self.write(f"RIGHT: {self.right_score}", False, align="center", font=('Arial', 24, 'normal'))
        self.goto(100,200)
        self.write(f"LEFT: {self.left_score}", False, align="center", font=('Arial', 24, 'normal'))

    def add_right_score(self):
        """_summary_
        """
        self.right_score +=1
        self.update_score()
    
    def add_left_score(self):
        """_summary_
        """
        self.left_score +=1
        self.update_score()
      





