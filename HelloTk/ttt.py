from tkinter import *

player = 'X'

def button_action(button, row, col):
    global player
    button.configure(text=player)
    button.configure(state=DISABLED)
    player = 'X' if player == 'O' else 'O'
    print("Button " + str(row) + " " + str(col) + " clicked")

# board = [
#     ['X', ' ', 'O'],
#     ['X', 'X', 'O'],
#     [' ', 'O', ' ']
# ]

window = Tk()

for row in range(3):
    for col in range(3):
        btn = Button(window, text=' ')
        btn.configure(command=lambda b=btn, r=row, c=col: button_action(b, r, c))
        btn.grid(column=col, row=row)

window.mainloop()