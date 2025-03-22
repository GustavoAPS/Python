from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=400)
screen.listen()
screen.bgcolor("black")
screen.title("PONG")
right_paddle = Paddle(side="right")
left_paddle = Paddle(side="left")
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 270:
        ball.horizontal_bounce()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -270:
        ball.horizontal_bounce()

    if ball.xcor() > 300:
        scoreboard.add_l_point()
        ball.reset_position()

    if ball.xcor() < -300:
        scoreboard.add_r_point()
        ball.reset_position()

    time.sleep(0.1)
screen.exitonclick()
