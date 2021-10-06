from tkinter import *

player = 'X'

def button_action(event, row, col):
    global player
    label = event.widget
    label.unbind("<Button>")
    label.configure(bg='gray')
    player = 'X' if player == 'O' else 'O'
    label.configure(text=player)

board = [
    ['X', ' ', 'O'],
    ['X', 'X', 'O'],
    [' ', 'O', ' ']
]

window = Tk()

for row in range(3):
    for col in range(3):
        label = Label(window, text=' ', font='Arial 40', bg='cyan',
                      height=2, width=4, relief=RAISED)
        label.bind("<Button>", lambda event, r=row, c=col: button_action(event, r, c))
        label.grid(column=col, row=row)

window.mainloop()