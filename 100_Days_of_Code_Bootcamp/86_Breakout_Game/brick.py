from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, pos_x, pos_y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=5)

        # initial position of paddle
        self.goto(pos_x, pos_y)
