from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
# reading data from french csv using pandas
current_card = {}
to_learn = {}
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bk, image=old_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(card_bk, image=new_image)
    canvas.itemconfig(language, fill="white")
    canvas.itemconfig(word, fill="white")


def is_known():
    to_learn.remove(current_card)
    data_to_learn = DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Canvas
canvas = Canvas(width=800, height=526)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
card_bk = canvas.create_image(400, 263, image=old_image)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)
# Buttons
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")
button_x = Button(image=wrong, highlightthickness=0, command=next_card)
button_x.grid(column=0, row=1)
button_y = Button(image=right, highlightthickness=0, command=is_known)
button_y.grid(column=1, row=1)

next_card()

window.mainloop()
