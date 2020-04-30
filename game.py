import os
import models
import exceptions
import settings


def start(name):
    player = models.Player(name)
    level = 1
    enemy = models.Enemy(level)
    while True:
        attack = 0
        while str(attack) not in ['1', '2', '3']:
            attack = input('Choose fighter. Enter "1" for Waterbender, "2" for Firebender, "3" for Earthbender: ')

        player.actor = int(attack)
        enemy.select_attack()

        try:
            print('_'*46)
            attack_result = player.attack(enemy)
            print(attack_result)
            defence_result = player.defence(enemy)
            print(defence_result)
            print('_'*46)

        except exceptions.EnemyDown:
            level += 1
            player.score += 5
            print("You attacked successfully! Score is {}".format(player.score))
            print("{} wins! Level up to {}.".format(name, level))
            print('______________________________________________')
            enemy = models.Enemy(level)
        except exceptions.GameOver:
            print("You were hit!")
            print('{} dies! Score is {}.'.format(name, player.score))
            exceptions.GameOver.add_score(name, player.score)
            raise exceptions.GameOver


def show_help():
    print(settings.ALLOWED_COMMAND)


def show_scores():
    with open('scores.txt', 'r') as f:
        if os.path.getsize('scores.txt') == 0:
            print('There are no results yet!')
        else:
            line = f.readlines()
            print(' '.join(line))


def play():
    name = input('Enter your Name: ')
    while True:
        act = input('Enter "Start" for beginning or "Help" for command list: ')
        act = act.lower()
        if act == "start":
            start(name)
        elif act == 'show scores':
            show_scores()
        elif act == "exit":
            raise exceptions.GameOver
        else:
            show_help()


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver as err:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
