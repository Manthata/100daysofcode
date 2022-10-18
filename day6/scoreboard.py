from turtle import Turtle

class Scoreboard(Turtle):
    """_summary_

    Args:
        Turtle (_type_): _description_
    """

    def __init__(self,) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-100, 260)
        self.update_score()
        self.hideturtle()

        
    def update_score(self):
        """_summary_
        """
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 24, 'normal'))

