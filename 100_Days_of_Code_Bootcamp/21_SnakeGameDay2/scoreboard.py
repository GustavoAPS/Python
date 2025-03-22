from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_score()

    def read_high_score_from_file(self):
        with open("data.txt") as file:
            contents = file.read()
            self.high_score = int(contents)

    def write_high_score_to_file(self, score):
        with open("data.txt", mode='w') as file:
            file.write(str(score))

    def update_score(self):
        self.clear()
        score_text = "Score: "+str(self.score)+" High score:"+str(self.high_score)
        self.write(arg=score_text, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_file(self.score)
        self.score = 0
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_score()
