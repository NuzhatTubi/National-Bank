from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x300")
window.title("Inches to Centimeters Converter")

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"Result: {cm} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create and place the widgets
label = Label(window, text="Enter length in inches:")
label.pack()

entry = Entry(window)
entry.pack()

convert_button = Button(window, text="Convert", command=convert_to_cm)
convert_button.pack()

result_label = Label(window, text="Result:")
result_label.pack()

window.mainloop()
