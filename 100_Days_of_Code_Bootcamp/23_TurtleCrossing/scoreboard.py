from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.write_score()


    def write_score(self):
        self.clear()
        self.setpos(-150, 160)
        self.write(f"Score:{self.score}", True, align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def add_score(self):
        self.score += 100
        self.write_score()

    def write_game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write("GAME OVER", True, align="center", font=("Courier", 40, "normal"))
        self.hideturtle()
