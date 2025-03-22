from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    count_down(25 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    num_minutes = math.floor(count/60)
    num_seconds = count % 60
    if num_seconds < 10:
        num_seconds = f"0{num_seconds}"
    canvas.itemconfig(timer_text, text=f"{num_minutes}:{num_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(widt=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

pomodoros_done_label = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
pomodoros_done_label.grid(row=3, column=1)

reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 15, "bold"))
reset_button.grid(row=2, column=2)


window.mainloop()
