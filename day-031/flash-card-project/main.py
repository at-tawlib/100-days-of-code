from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}   # to hold the current card
to_learn = {}       # to hold list of unknown cards

try:
    # get data from words_to_learn.csv
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # if file not found, read from the original file
    original_data = pandas.read_csv("data/french_words.csv")
    # convert data to list of dictionary [{english: word, french:word}]
    to_learn = original_data.to_dict(orient="records")
else:
    # convert data to list of dictionary [{english: word, french:word}]
    to_learn = data.to_dict(orient="records")

def next_card():
    """show the next random card"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel the timer
    current_card = random.choice(to_learn)  # get the next random card
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)  # wait for 3 seconds then flip the card

def flip_card():
    """flip the card to show the English translation"""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)

def is_known():
    """remove the card from the list"""
    to_learn.remove(current_card)
    # save remaining cards into a new file to load when app starts
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# -------------------------- UI ------------------------------------
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# get photo images
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# set up canvas
canvas = Canvas(height=600, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 300, image=card_back_img)
card_title = canvas.create_text(400, 200, text="", font=("Arial", 30, "italic"))
card_text = canvas.create_text(400, 300, text="", font=("Arial", 50, "bold"))

# create buttons
btn_known = Button(image=right_img, command=is_known)
btn_unknown = Button(image=wrong_img, command=next_card)

# position widgets
canvas.grid(row=0, column=0, columnspan=2)
btn_known.grid(row=1, column=1)
btn_unknown.grid(row=1, column=0)

next_card()

window.mainloop()
