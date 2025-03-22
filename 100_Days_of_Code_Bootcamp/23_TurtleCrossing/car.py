from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.penup()
        self.setpos(random.randint(-225, 225), random.randint(-100, 100))

    def move(self):
        new_x_position = self.xcor() - 10
        self.setpos(new_x_position, self.ycor())

    def set_random_y(self):
        self.setpos(225, random.randint(-100, 100))

