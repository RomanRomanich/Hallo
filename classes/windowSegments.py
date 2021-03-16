import tkinter as tk


def win_update():
    window.update()


def sleep(millisecond, function):
    message_text.update()
    window.after(millisecond, function)


window = tk.Tk()
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry('600x400+%d+%d' % (x, y))
window.title("Game")


# настройка части интерфейса текста
message_frame = tk.Frame(window, relief='raised', borderwidth=2)
message_frame.grid(row=0, column=1, sticky='nwes')
message_text = tk.Label(message_frame,
                        # text='Enemy',
                        bg="red",
                        fg="white",
                        width=50)
message_text.pack(fill='both')
message_text2 = tk.Label(message_frame,
                        # text='Enemy1',
                        bg="green",
                        fg="black",
                        width=50)
message_text2.pack(fill='both')


# настройка части интерфейса игрока
player_frame = tk.Frame(window, relief='raised', borderwidth=2)
player_frame.grid(row=0, column=0, sticky='nwes')
player_name = tk.Label(player_frame, fg='black')
player_name.pack()
player_hp = tk.Label(player_frame, fg="green")
player_hp.pack()


# настройка части интерфейса противника
enemy_frame = tk.Frame(window, relief='raised', borderwidth=2)
enemy_frame.grid(row=0, column=2, sticky='nwes')
enemy_name = tk.Label(enemy_frame, fg='red')
enemy_name.pack()
enemy_hp = tk.Label(enemy_frame, fg='black')
enemy_hp.pack()


# настройка части интерфейса кнопок
button_frame = tk.Frame(window, relief='raised', borderwidth=2)
button_frame.grid(row=1, columnspan=3, sticky='we')

attack_button = tk.Button(button_frame,
                          text="attack",
                          bg="darkgrey",
                          fg="white")
attack_button.grid(row=1, column=0)
defense_button = tk.Button(button_frame,
                           text="defense",
                           bg="darkgrey",
                           fg="white")
defense_button.grid(row=1, column=1)
start_button = tk.Button(button_frame,
                         text='Start',
                         bg="darkgrey",
                         fg="white")
start_button.grid(row=1, column=2)





size_of_grid = window.grid_size()

for columns in range(size_of_grid[0]):
    window.columnconfigure(columns, weight=1)


for rows in range(size_of_grid[1]):
    window.rowconfigure(rows, weight=1)

