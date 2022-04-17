from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


def generator_button():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)
    random_password = "".join(password_list)
    word.insert(END, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    webinfo = web.get()
    userinfo = mail.get()
    password_info = word.get()
    new_data = {
        webinfo: {
            "email": userinfo,
            "password": password_info,
        }
    }
    if (len(webinfo) == 0) or (len(userinfo) == 0) or (len(password_info) == 0):
        messagebox.showerror(title="Error", message="Not all fields are filled")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web.delete(0, END)
            word.delete(0, END)


def find_password():
    website_search = web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"{website_search} does not exist in database")
    else:
        if website_search in data:
            email_search = data[website_search]["email"]
            password_search = data[website_search]["password"]
            messagebox.showinfo(title=website_search, message=f"Email: {email_search}\nPassword: {password_search}")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
My_Pass = PhotoImage(file="logo.png")
canvas.create_image(50, 94, image=My_Pass)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
# Entry
web = Entry(width=18)
web.place(x=119, y=195)
web.focus()

mail = Entry(width=35)
mail.grid(column=1, row=2, columnspan=2)
mail.insert(0, string="assemzhar@icloud.com")

word = Entry(width=18)
word.place(x=119, y=245)

# Button
generator = Button(text="Generate Password", width=13, height=1, highlightthickness=0, command=generator_button)
generator.config(pady=5)
generator.place(x=270, y=245)

add_button = Button(text="Add", width=33, command=add_button)
add_button.place(x=114, y=275)

search_button = Button(text="Search", width=13, highlightthickness=0, command=find_password)
search_button.config(pady=5)
search_button.place(x=270, y=190)

window.mainloop()
