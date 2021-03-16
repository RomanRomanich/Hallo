import random


class Creature():

    def __init__(self, creatureName, creatureType, creatureLevel=1):
        self.creatureName = creatureName
        self.creatureType = creatureType
        self.creatureLevel = creatureLevel
        self.creatureEnergy = 50
        self.creatureAgility = 1
        self.creatureHealth = 50
        self.creatureStrenght = 1



class Player(Creature):

    def attack(self, window_element, enemy='enemy1'):
        damage = random.randint(1, 6)
        if hasattr(enemy, 'creatureName'):
            enemy.creatureHealth -= damage
            window_element.message_text['text'] = f'You hit {enemy.creatureName} at {damage} HP'
            window_element.enemy_hp['text'] = enemy.creatureHealth
        else:
            window_element.message_text['text'] = f'You hit {enemy} at {damage} HP'
        window_element.message_text.update()

class Enemy(Creature):

    def attack(self, window_element, player='enemy'):
        damage = random.randint(1, 6)
        window_element.message_text2['text'] = f'{self.creatureName} hit {player.creatureName} at {damage} HP'