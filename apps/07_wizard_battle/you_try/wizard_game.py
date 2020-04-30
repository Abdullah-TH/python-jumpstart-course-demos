import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------------')
    print('      WIZARD GAME APP')
    print('------------------------------')
    print('')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, False),
        Dragon('Dragon', 50, True),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature} has appear from a dark and a foggy forest...')
        command = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

        if command == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover')
                time.sleep(5)
                print('The wizard returns revitalized!')

        elif command == 'r':
            print('The wizard has becomes unsure of his power and flees!')

        elif command == 'l':
            print(f'The wizard {hero.name} takes in the surrounding and sees: ')
            for creature in creatures:
                print(creature)

        else:
            print('OK, exiting game..... bye!')
            break

        print()
        if not creatures:
            print('You defeated all creatures! you WON!')
            break


if __name__ == '__main__':
    main()
