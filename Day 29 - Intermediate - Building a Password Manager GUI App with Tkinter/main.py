from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for _ in range(random.randint(8, 10))] +
                     [random.choice(symbols) for _ in range(random.randint(2, 4))] +
                     [random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)
    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_field.get().title():{
            "email":email_field.get(),
            "password": password_field.get()
        }
    }
    if not website_field.get() or not password_field.get():
        messagebox.showinfo(title="Empty", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        website_field.delete(0, END)
        password_field.delete(0, END)

# ------------------------- SEARCH PASSWORD ------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Missing File", message="data.json not found")
    else:
        if website_field.get() in data:
            messagebox.showinfo(title=website_field.get(),
                                message=f"Email: {data[website_field.get().title()]["email"]}\n"
                                        f""f"Password: {data[website_field.get().title()]["password"]}")
        else:
            messagebox.showinfo(title="Not Found", message="No results Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_field = Entry(width= 24)
website_field.grid(column=1, row=1, columnspan=2, sticky="w")
website_field.focus()

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1, sticky="w")

email_field = Entry(width= 43)
email_field.grid(column=1, row=2, columnspan=2, sticky="w")
email_field.insert(0, "fellipe@email.com")

password_field = Entry(width=24)
password_field.grid(column=1, row=3, columnspan=2, sticky="w")

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
window.mainloop()