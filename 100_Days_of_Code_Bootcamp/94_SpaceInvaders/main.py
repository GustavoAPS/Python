from turtle import Screen
from player import Player
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Space Invaders")

player = Player()



screen.exitonclick()
