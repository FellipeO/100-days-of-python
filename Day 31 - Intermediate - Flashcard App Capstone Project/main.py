from textwrap import fill

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

# --------------------------- CARD LOGIC ------------------------------ #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_card["English"], fill="white")

def green_button():
    global words_to_learn
    words_to_learn = [word for word in words_to_learn if word["French"] != new_card["French"]]
    new_df = pd.DataFrame(words_to_learn)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global new_card, cd_timer
    window.after_cancel(cd_timer)
    new_card = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text= "French", fill="black")
    canvas.itemconfig(word_text, text=new_card["French"], fill="black")
    cd_timer = window.after(3000, flip_card)

# ----------------------------- SETUP -------------------------------- #
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
words_to_learn = df.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400 ,263 ,image=card_front_img)
canvas.grid(column=1, row=1, columnspan=2)
language_text = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word_text = canvas.create_text(400, 263,text="", font=("arial", 60, "bold"))

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=green_button)
right_button.grid(column=2, row=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)

cd_timer = window.after(3000, flip_card)

next_card()

window.mainloop()
