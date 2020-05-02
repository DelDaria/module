import random
import exceptions
import settings
from datetime import datetime


class Enemy:
    level = None
    lives = None
    actor = None

    def __init__(self, level):
        self.level = level
        self.lives = level

    def select_attack(self):
        random.seed(datetime.now())
        self.actor = random.randint(1, 3)

    def decrease_lives(self):
        if self.lives > 1:
            self.lives -= 1
        else:
            raise exceptions.EnemyDown


class Player:
    name = None
    lives = None
    score = 0
    actor = None

    def __init__(self, name):
        self.name = name
        self.lives = settings.LIVES

    @staticmethod
    def fight(attack_side, defense_side):
        if attack_side.actor == defense_side.actor:
            return 0
        elif attack_side.actor == 3 and defense_side.actor == 1:
            return 1
        elif attack_side.actor < defense_side.actor:
            return 1
        else:
            return -1

    def decrease_lives(self):
        if self.lives > 1:
            self.lives -= 1
        else:
            raise exceptions.GameOver

    def attack(self, enemy):
        res = self.fight(self, enemy)
        if res == 0:
            return "It's a draw!"
        elif res == 1:
            self.score += 1
            enemy.decrease_lives()
            return "You attacked successfully! Score is {}".format(self.score)
        elif res == -1:
            return "You missed!"

    def defence(self, enemy):
        res = self.fight(enemy, self)
        if res == 0:
            return "It's a draw!"
        elif res == 1:
            self.decrease_lives()
            return "You were hit!"
        elif res == -1:
            return "You evaded!"
