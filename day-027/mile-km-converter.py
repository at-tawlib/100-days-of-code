# mile to km converter
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)

mile_input = Entry(width=5)
label_miles = Label(text="Miles")
label_is_equal = Label(text="is equal to")
label_km_value = Label(text="0")
label_km = Label(text="Km")
button = Button(text="Calculate")

# place the widgets
mile_input.grid(column=2, row=0)
label_miles.grid(column=3, row=0)
label_is_equal.grid(column=0, row=2)
label_km_value.grid(column=2, row=2)
label_km.grid(column=3, row=2)
button.grid(column=2, row=3)


def convert():
    mile = mile_input.get()
    km_value = int(mile) * 1.60934
    label_km_value.config(text=f"{km_value}")


button.config(command=convert)
window.mainloop()
