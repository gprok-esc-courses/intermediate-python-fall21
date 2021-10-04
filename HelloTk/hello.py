from tkinter import *


def button_action():
    txt = field.get()
    label.configure(text=txt)


window = Tk()
window.title("Hello App")
window.geometry("600x400")

label = Label(window, text='Hello World!', bg='black', fg='white')
label.grid(column=0, row=0)

button = Button(window, text="Click Me", command=button_action)
button.grid(column=1, row=1)

field = Entry(window, width=10)
field.grid(column=0, row=1)

canvas = Canvas(window)
canvas.grid(column=0, row=2)
line = canvas.create_line(1, 1, 100, 100)

window.mainloop()
