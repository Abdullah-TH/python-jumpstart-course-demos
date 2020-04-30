import random


class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature: Creature):
        print(f'The wizard {self.name} attacks {creature.name}')

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f'You roll {my_roll}...')
        print(f'The creature rolls {creature_roll}...')

        if my_roll >= creature_roll:
            print(f'The wizard {self.name} has handily defeated {creature.name}')
            return True
        else:
            print('The wizard has be DEFEATED!!!')
            return False


class SmallAnimal(Creature):

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll // 2


class Dragon(Creature):

    def __init__(self, name, level, breath_fire):
        super().__init__(name, level)
        self.breath_fire = breath_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breath_fire else 1
        return base_roll * fire_modifier

    def __repr__(self):
        if self.breath_fire:
            return super().__repr__() + ' that breath FIRE!'
        else:
            return super().__repr__()
