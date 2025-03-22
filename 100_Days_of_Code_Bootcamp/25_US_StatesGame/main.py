import turtle
import pandas as pd


data = pd.read_csv("50_states.csv")

text_drawer = turtle.Turtle()

screen = turtle.Screen()
screen.title("US.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

text_drawer.color("black")
text_drawer.penup()
text_drawer.hideturtle()
text_drawer.clear()
game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

    for i in range(0, 50):
        if data.state[i] == answer_state:
            print("bingo")
            text_drawer.goto(data.x[i], data.y[i])
            text_drawer.write(data.state[i], align="center", font=("Courier", 15, "normal"))

turtle.mainloop()
# screen.exitonclick()
