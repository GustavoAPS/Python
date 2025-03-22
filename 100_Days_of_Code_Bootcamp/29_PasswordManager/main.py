from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ----------------------- PASSWORD GENERATOR --------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #Use list comprehension
    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ----------------------- SAVE PASSWORD -------------------------- #
def save():
    # website user password
    website_name = web_site_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()
    entry = website_name+" | "+user_name+" | "+password + '\n'

    is_ok = messagebox.askokcancel(title="Status", message=f"Are your informations correct?\n"
                                                   f"{website_name}\n{user_name}"
                                                   f"\n{password}")
    if len(website_name) > 0 and len(user_name) and len(password):
        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(entry)
            web_site_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Error", message="Empty fields")
# ----------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

web_site_label = Label(text="Website:")
web_site_label.grid(row=1, column=0)
web_site_entry = Entry(width=35)
web_site_entry.focus()
web_site_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=16, show="*")
password_entry.grid(row=3, column=1, columnspan=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
