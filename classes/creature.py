import random
# общий клас существ

class Creature():
    enemy_name = ['Wolf', 'Tiger', 'Panter']

    def __init__(self, creature_name = None, creature_type = None, creature_level=1):
        if creature_name:
            self.creature_name = creature_name
        else:
            self.creature_name = Creature.enemy_name[random.randint(0, 2)]
        self.creature_type = creature_type
        self.creature_level = creature_level
        self.creature_energy = 50
        self.creature_agility = 1
        self.creature_health = 50
        self.creature_strenght = 1


class Player(Creature):
    def attack(self, window_element, enemy='enemy1'):
        damage = random.randint(1, 6)
        enemy.creature_health -= damage
        if enemy.creature_health > 0:
            window_element.message_text['text'] = f'You hit {enemy.creature_name} at {damage} HP'
            # window_element.message_text['text'] = f'You hit {enemy.creature_name} at {damage} HP'
            window_element.enemy_hp['text'] = enemy.creature_health
        else:
            window_element.message_text['text'] = f'Yuo hit {enemy.creature_name} at {damage} HP. {enemy.creature_name} is dead'
            window_element.enemy_hp['text'] = 0
        window_element.message_text.update()


class Enemy(Creature):
    def attack(self, window_element, player='Player1'):
        damage = random.randint(6, 6)
        player.creature_health -= damage
        if player.creature_health > 0:
            window_element.message_text2['text'] = f'{self.creature_name} hit {player.creature_name} at {damage} HP'
            window_element.player_hp['text'] = player.creature_health
        else:
            window_element.message_text2['text'] = f'{self.creature_name} hit {player.creature_name} at {damage} HP. ' \
                                                   f'You are dead '
            window_element.player_hp['text'] = 0
