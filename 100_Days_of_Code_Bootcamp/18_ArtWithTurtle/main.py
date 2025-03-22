import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors_tuple = (r, g, b)
    return colors_tuple


local_turtle = Turtle()
local_turtle.color("blue")
local_turtle.pensize(1)
turtle.colormode(255)
local_turtle.pencolor(random_color())
local_turtle.speed("fastest")

for _ in range(1, 91):
    local_turtle.circle(60)
    local_turtle.left(360/_)
    local_turtle.pencolor(random_color())

screen = Screen()
screen.exitonclick()
