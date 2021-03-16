from classes.loader import *


player = None
enemy = None
enemy_name = ['Wolf', 'Tiger', 'Panter']


print(player, enemy)


def combat_circle():
    player.attack(winElements, enemy)
    winElements.window.after(1000, enemy.attack(winElements, player))


def new_player():
    player = creature.Player('New Player', 'human')
    return player


def new_enemy(name):
    enemy = creature.Enemy(name, 'wolf')
    return enemy


def new_start():
    global enemy
    global player
    player = new_player()
    enemy = new_enemy(enemy_name[random.randint(0, 2)])



if not player and not enemy:
    print('Var not defined')
    winElements.start_button['command'] = new_start
    # winElements.window.update()
    # player = new_player()
    # enemy = new_enemy(enemy_name[random.randint(0, 2)])
    # new_start()
    print(player, enemy)
if player and enemy:
    winElements.player_name['text'] = player.creatureName
    winElements.player_hp['text'] = player.creatureHealth

    winElements.enemy_name['text'] = enemy.creatureName
    winElements.enemy_hp['text'] = enemy.creatureHealth

    winElements.attack_button['command'] = combat_circle
    print(player, enemy)






# player = new_player()
# enemy = new_enemy('wolf')







winElements.window.mainloop()