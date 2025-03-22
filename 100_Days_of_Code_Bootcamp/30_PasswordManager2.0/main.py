from tkinter import *
from tkinter import messagebox
import random
import json


# ----------------------- PASSWORD GENERATOR --------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

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


def save():
    # website user password
    website_name = web_site_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()
    new_data = {website_name: {
                        "username": user_name,
                        "password": password,
                    }
                }

    if len(website_name) > 0 and len(user_name) and len(password):
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_site_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Error", message="Empty fields")
# ------------------------ Search -------------------------------- #


def search():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
        site_name = web_site_entry.get()
        search_data = data[site_name]
        print(search_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Entry not found")
    except KeyError:
        print("Key not found")

    else:
        messagebox.showinfo(title=f"{site_name}", message=f"Username: {search_data['username']}\nPassword: {search_data['password']}")

    finally:
        print("done")
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
web_site_entry.grid(row=1, column=1, columnspan=1)
web_site_button = Button(text="Search", command=search, width=15)
web_site_button.grid(row=1, column=2, columnspan=1)

email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column=0)
email_entry = Entry(width= 35)
email_entry.grid(row=2, column=1, columnspan=1)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=35, show="*")
password_entry.grid(row=3, column=1, columnspan=1)
password_button = Button(text="Generate Password", command=generate_password, width=15)
password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=1)


window.mainloop()
