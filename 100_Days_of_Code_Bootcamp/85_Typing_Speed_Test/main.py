import tkinter as tk
import tkinter.messagebox
import time


def stop_typing(self):
    print("typing stopped")

    # this has to be measured from the input text not the fixed one.
    word_list = quotes[0].split()
    number_of_words = len(word_list)

    text_input.focus_set()
    end = time.time()

    a_float = (number_of_words / (end - start))*60
    formatted_float = "{:.2f}".format(a_float)

    tkinter.messagebox.showinfo("Results", f"Hi, your typing speed is { formatted_float } per minute")

quotes = ["I’m going to defeat you with the power of friendship", "You know how I roll.", "If you can’t beat them, dress better than them"]

start = time.time()

window = tk.Tk()
window.title("Typing Speed Test")

window.bind('<Return>', stop_typing)
label = tk.Label(window, text=quotes[0])
text_input = tk.Text(window, width=38, height=6)

label.grid(row=0, column=0, pady=(10, 10))
text_input.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

window.mainloop()
