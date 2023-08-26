from tkinter import *

# Creates a window using the Tk() class in the tkinter package.
window = Tk()

# Gives a title to the window.
window.title("Is this GUI?")

# Sets up the window with a minimum width of 500 and minimum height of 300.
window.minsize(width=500, height=300)

# To add padding in the window along the x-axis and the y-axis.
window.config(padx=20, pady=20)

# Create a label using the Label class in the tkinter package.
label = Label(text="Am I a Label?", font=("Arial", 15, "bold italic"))

# To place the label in the window.
label.grid(row=0, column=0)


# label["text"] = "I am a Label."
# OR
# label.config(text="I am a Label.")

def on_button_click():
    label["text"] = entry.get()


# Create a button using the Button class in the tkinter package.
button = Button(height=1, width=12, text="Click Me", command=on_button_click)
button.grid(row=1, column=1)

button2 = Button(height=1, width=12, text="Click Me Too")
button2.grid(row=0, column=2)

# Create an input field using the Entry class in the tkinter package.

entry = Entry(width=12)
entry.grid(row=3, column=3)

# To keep the window on screen use the mainloop() function.
window.mainloop()
