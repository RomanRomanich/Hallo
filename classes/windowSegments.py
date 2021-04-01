import tkinter as tk
from classes.loader import *

class Window(tk.Tk, object):
    def __init__(self, window):
        self.window = window
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
        self.window.wm_geometry('600x400+%d+%d' % (x, y))
        self.window.title("Game")
# настройка части интерфейса текста
        self.message_frame = tk.Frame(self.window, relief='raised', borderwidth=2)
        self.message_frame.grid(row=0, column=1, sticky='nwes')
        self.message_text = tk.Label(self.message_frame,
                                # text='Enemy',
                                bg="red",
                                fg="white",
                                width=50)
        self.message_text.pack(fill='both')
        self.message_text2 = tk.Label(self.message_frame,
                                # text='Enemy1',
                                bg="green",
                                fg="black",
                                width=50)
        self.message_text2.pack(fill='both')
# настройка части интерфейса игрока
        self.player_frame = tk.Frame(self.window, relief='raised', borderwidth=2)
        self.player_frame.grid(row=0, column=0, sticky='nwes')
        self.player_name = tk.Label(self.player_frame, fg='black')
        self.player_name.pack()
        self.player_hp = tk.Label(self.player_frame, fg="green")
        self.player_hp.pack()
# настройка части интерфейса противника
        self.enemy_frame = tk.Frame(self.window, relief='raised', borderwidth=2)
        self.enemy_frame.grid(row=0, column=2, sticky='nwes')
        self.enemy_name = tk.Label(self.enemy_frame, fg='red')
        self.enemy_name.pack()
        self.enemy_hp = tk.Label(self.enemy_frame, fg='black')
        self.enemy_hp.pack()
# настройка части интерфейса кнопок
        self.button_frame = tk.Frame(self.window, relief='raised', borderwidth=2)
        self.button_frame.grid(row=1, columnspan=3, sticky='we')
# Кнопка атаки
        self.attack_button = tk.Button(self.button_frame,
                                    text="attack",
                                    bg="darkgrey",
                                    fg="white",)
        self.attack_button.grid(row=1, column=0)
# Кнопка защиты
        self.defense_button = tk.Button(self.button_frame,
                                   text="defense",
                                   bg="darkgrey",
                                   fg="white")
        self.defense_button.grid(row=1, column=1)
# Кнопка старт
        self.start_button = tk.Button(self.button_frame,
                                    text='Start',
                                    bg="darkgrey",
                                    fg="white",
                                    command=self.start_new_game)
        self.start_button.grid(row=1, column=2)

# настройка растягивания колонок и столбцов
        self.size_of_grid = self.window.grid_size()
        for columns in range(self.size_of_grid[0]):
            self.window.columnconfigure(columns, weight=1)
        for rows in range(self.size_of_grid[1]):
            self.window.rowconfigure(rows, weight=1)
# старт основного цикла программы
        self.window.mainloop()
# старт новой игры
    def start_new_game(self):
        self.player = creature.Player('Player1','Human')
        # self.enemy = creature.Enemy('Wolf','Wolf')
        self.enemy = creature.Enemy()
        self.set_elements_to_window()
# размещение элементоы управления на главном экране
    def set_elements_to_window(self):
        self.player_name['text'] = self.player.creature_name
        self.player_hp['text'] = self.player.creature_health
        self.enemy_hp['text'] = self.enemy.creature_health
        self.enemy_name['text'] = self.enemy.creature_name
        self.attack_button['command'] = self.combat_circle
# основной боевой цикл
    def combat_circle(self):
        if self.player.creature_health > 0 or self.enemy.creature_health > 0:
            if self.player.creature_health > 0:
                self.player.attack(self, self.enemy)
            if self.enemy.creature_health > 0:
                self.window.after(300, self.enemy.attack(self, self.player))