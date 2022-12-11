# using grid to place widgets
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# padding around label
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Button")
button.grid(column=2, row=2)

# Button
new_button = Button(text="New Button")
new_button.grid(column=3, row=1)

# Entry
input_ = Entry(width=18)
print(input_.get())
input_.grid(column=4, row=4)

# Adding padding to the window
window.config(padx=100, pady=200)

window.mainloop()
