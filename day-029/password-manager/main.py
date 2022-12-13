# Day 029(13-12-2022) Password Generator
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password generator from Day 5
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # get 8, 9 or 10 letters
    password_letters = [choice(letters) for _ in range(randint(8, 10)) ]
    # get 2, 3 or 4 symbols
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # get 2, 3 or 4 numbers
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    # copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:"
                            f"{email}\n"
                            f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{entry_website.get()} | {entry_email.get()} | {entry_password.get()}\n")
                entry_password.delete(0, END)
                entry_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

label_website = Label(text="Website:")
label_email = Label(text="Email/Username:")
label_password = Label(text="Password:")

entry_website = Entry(width=40)
entry_website.focus()
entry_email = Entry(width=40)
entry_password = Entry(width=21)

btn_gen_password = Button(text="Generate Password", command=generate_password)
btn_add = Button(text="Add", width=36, command=save)

# place widgets
canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
label_email.grid(column=0, row=2)
label_password.grid(column=0, row=3)
entry_website.grid(column=1, row=1, columnspan=2)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "dealrega@yahoo.com")
entry_password.grid(column=1, row=3)
btn_add.grid(column=1, row=4, columnspan=2)
btn_gen_password.grid(column=2, row=3)

window.mainloop()