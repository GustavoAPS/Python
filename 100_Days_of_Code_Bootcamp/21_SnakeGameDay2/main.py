from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        print("Food eaten")
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280:
        scoreboard.reset()
        snake.reset()
    if snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail:
    for segment in snake.snake_body[1:]:
        # if segment == snake.snake_body[0]:
        #     pass
        if snake.snake_body[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
