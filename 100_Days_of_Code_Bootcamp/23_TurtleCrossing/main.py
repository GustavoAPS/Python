from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time


screen = Screen()
screen.setup(width=450, height=400)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    screen.update()

    if car_manager.check_if_hit_player(player):
        scoreboard.write_game_over()
        game_is_on = False
    else:
        car_manager.move_cars()

        if player.ycor() > 140:
            # game_is_on = False
            scoreboard.add_score()
            player.reset_position()

    time.sleep(0.1)

screen.exitonclick()
