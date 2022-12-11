# day -0 27
from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(expand=True)
# my_label.pack(side="bottom")
my_label.pack()

# different ways of using label with text
my_label["text"] = "New Text"
my_label.config(text="New Text")

# input
input_ = Entry()
input_.pack()


def button_clicked():
    print("I got clicked")
    my_label.config(text=input_.get())


# Add button
button = Button(text="Click", command=button_clicked)
button.pack()

window.mainloop()
