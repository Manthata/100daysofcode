

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """_summary_

    Args:
        Turtle (_type_): Turtle class
    """

    def __init__(self) -> None:
        super().__init__()

        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()
    

    def update_score(self):
        """_summary_
        """
        self.clear()
        self.goto(-200,250)
        self.write(f"level: {self.level}", False, align="center", font= FONT)

    def add_level(self):
        """_summary_
        """
        self.level +=1
        self.update_score()
    
    def game_over(self):
        """_summary_
        """
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=('Arial', 24, 'normal')) 
        self.hideturtle()

    

      




