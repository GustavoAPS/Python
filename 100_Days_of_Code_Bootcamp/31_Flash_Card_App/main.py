from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


def flip_card(entry):
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=entry["English"])


def next_card():
    data = pd.read_csv("data/french_words.csv")
    my_dict = data.to_dict(orient="records")
    entry = random.choice(my_dict)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=entry["French"])
    window.after(3000, flip_card, entry)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=15, pady=15)

canvas = Canvas(width=400, height=250)
canvas.grid(row=0, column=0, columnspan=2)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas_image = canvas.create_image(200, 125, image=card_front_image)

title = canvas.create_text(200, 50, text="Title", font=("Ariel", 20, "italic"))
word = canvas.create_text(200, 150, text="Word", font=("Ariel", 30, "bold"))

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
