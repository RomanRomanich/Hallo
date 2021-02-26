import tkinter as tk
import random
import sys
from functools import partial
from classes import creature

def playerAtack(windowElement, enemy='enemy1'):
    damage = random.randint(1, 6)
    windowElement['text'] = f'You hit {enemy} at {damage} HP'


window = tk.Tk()
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry('400x250+%d+%d' % (x, y))
window.title("test")
labelText = tk.Label(window,
                     text='Enemy',
                     bg="red",
                     fg="white",
                     width=50)
attackButton = tk.Button(window,
                         text="attack",
                         bg="darkgrey",
                         fg="white",
                         command=partial(playerAtack, labelText))
defenseButton = tk.Button(window,
                          text="defense",
                         bg="darkgrey",
                         fg="white")


labelText.grid(row=0, columnspan=2)

attackButton.grid(row=1, column=1)
defenseButton.grid(row=1, column=0)
# print(dir(labelText))
# print(labelText.keys())
# print(labelText['text'])
# labelText['text'] = 'asd'
# attackButton.bind("<Button-1>", playerAtack(labelText))
# print(labelText['text'])
window.mainloop()
print(sys.path)