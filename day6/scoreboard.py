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
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def game_over(self):
        """ GAME OVER squence"""
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=('Arial', 24, 'normal')) 
        self.hideturtle()

    def update_scoreboard(self):
        """_summary_
        """
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 24, 'normal'))
    
    def update_score(self):
        """ Add one to the score when the snake collides with the food """
        self.score +=1
        self.clear()
        self.update_scoreboard()