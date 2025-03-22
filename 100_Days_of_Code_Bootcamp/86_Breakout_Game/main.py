from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.listen()
screen.bgcolor("black")
screen.title("Brick Breaker")

player_paddle = Paddle()
ball = Ball()

screen.onkey(player_paddle.go_right, "Right")
screen.onkey(player_paddle.go_left, "Left")

bricks = []
bricks_x_position = -190
for n in range(0, 4):
    red_brick = Brick(color='red', pos_x=bricks_x_position + n*125, pos_y=(SCREEN_HEIGHT/2) - 20)
    blue_brick = Brick(color='blue', pos_x=bricks_x_position + n*125, pos_y=(SCREEN_HEIGHT / 2) - 50)
    green_brick = Brick(color='green', pos_x=bricks_x_position + n*125, pos_y=(SCREEN_HEIGHT / 2) - 80)

    bricks.append(red_brick)
    bricks.append(blue_brick)
    bricks.append(green_brick)

game_is_on = True

while game_is_on:

    screen.update()
    ball.move()

    if ball.ycor() > (SCREEN_HEIGHT/2):
        ball.vertical_bounce()

    if ball.distance(player_paddle) < 50:
        ball.vertical_bounce()

    for brick in bricks:
        if ball.distance(brick) < 50:
            brick.goto(1000, 1000)
            ball.vertical_bounce()

    if ball.xcor() > SCREEN_WIDTH/2 or ball.xcor() < -1 * (SCREEN_WIDTH/2):
        ball.horizontal_bounce()



    time.sleep(0.1)

screen.exitonclick()
