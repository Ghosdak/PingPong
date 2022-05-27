from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
game_on = True

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or 
        ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    if ball.xcor() > 360:
        scoreboard.l_point()
        ball.reset()
        
    if ball.xcor() < -360:
        scoreboard.r_point()
        ball.reset()
        
screen.exitonclick()