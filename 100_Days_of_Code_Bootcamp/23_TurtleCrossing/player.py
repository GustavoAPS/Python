from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setpos(0, -180)

    def move(self):
        new_y_position = self.ycor() + 10
        self.setpos(0, new_y_position)

    def reset_position(self):
        self.setpos(0, -180)
