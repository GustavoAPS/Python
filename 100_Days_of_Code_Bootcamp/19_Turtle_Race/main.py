from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
start_position_x = -225
colors = ["red", "blue", "green", "yellow", "purple"]
turtles = []

for n in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(start_position_x, 100 - 50*n)
    turtles.append(new_turtle)

screen.listen()
user_bet = screen.textinput("Furious Turtles", "Enter the color of the winner")
if user_bet:
    isRaceOn = True

while isRaceOn:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your won, the winner is {winning_color}!!")
            else:
                print(f"Your lose, the winner is {winning_color}")
            isRaceOn = False
        else:
            rng_distance = random.randint(0, 10)
            turtle.forward(rng_distance)

screen.exitonclick()
