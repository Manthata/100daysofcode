from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


LEFT_INITIAL_POSITION = (-360,0)
RIGHT_INITIAL_POSITION = (360,0)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
left_paddle = Paddle(LEFT_INITIAL_POSITION)
right_paddle = Paddle(RIGHT_INITIAL_POSITION)
ball = Ball()
scoreboard = ScoreBoard()
# check for keyboard inputs 
screen.listen()
screen.onkey(left_paddle.move_down, "s")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(ball.start, "space")


game_is_om = True
while game_is_om:
    print(ball.move_speed)
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ball_move:
        ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 70 and ball.xcor() > 320:
        ball.bounce_x()
    
    if ball.distance(left_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 340:
        ball.reset()
        ball.stop()
        ball.bounce_x()
        scoreboard.add_right_score()
    
    if  ball.xcor() < -340:
        ball.reset()
        ball.bounce_x()
        scoreboard.add_left_score()
        

    


    
    
    

    
    



screen.exitonclick()
ball.stop()