import models
import exceptions


def play():
    name = input('Enter your Name: ')
    act = input('Enter "Start" for beginning or "Exit" for ending: ')
    if act.lower() == 'start':
        player = models.Player(name)
        level = 1
        enemy = models.Enemy(level)
        while True:
            attack = input('Choose fighter. Enter "1" for Waterbender, "2" for Firebender, "3" for Earthbender: ')
            player.actor = int(attack)
            enemy.select_attack()

            try:
                attack_result = player.attack(enemy)
                print(attack_result)
                defence_result = player.defence(enemy)
                print(defence_result)

            except exceptions.EnemyDown:
                level += 1
                player.score += 4
                print("{} wins! Level up to {}.".format(name, level))
                enemy = models.Enemy(level)
            except exceptions.GameOver:
                print('{} dies! Score is {}.'.format(name, player.score))
                # with open('scores.txt', 'a') as f:
                #     ps = str(player.score)
                #     for i in range(1, 11):
                #         f.write('{}: {}'.format(name, ps))
                #         f.write('\n')
                raise exceptions.GameOver
    elif act.lower() == 'exit':
        raise KeyboardInterrupt
    #else:



if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver as err:
        print('Player dies!')
        # TODO  записывает результат в таблицу рекордов.

    except KeyboardInterrupt:
        pass
    # except Exception as err:
    #     print(err.__class__.__name__)
    finally:
        print("Good bye!")
