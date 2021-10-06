from tkinter import *


def action(id):
    print("Button ", id, " is clicked")


window = Tk()

b1 = Button(window, text="Button 1", command=lambda: action(1))
b2 = Button(window, text="Button 2", command=lambda: action(2))

b1.pack()
b2.pack()

window.mainloop()
