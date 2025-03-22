from tkinter import *


window = Tk()
window.title("The Window")
window.minsize(width=300, height=100)


def print_message():
    label_2.config(text=str(float(my_input.get()) * 1.60934))


label_0 = Label(text="Miles")
label_0.grid(row=0, column=2)

my_input = Entry()
my_input.grid(row=0, column=1)

label_1 = Label(text="Is equal to")
label_1.grid(row=1, column=0)

label_2 = Label(text="0")
label_2.grid(row=1, column=1)

label_3 = Label(text="Km")
label_3.grid(row=1, column=2)

new_button = Button(text="Convert", command=print_message)
new_button.grid(row=2, column=1)

window.mainloop()
