
'''
AUTHOR - JARROD ULRICH
DATE -11/30/21
CLASS - ISTA 130
DESCRIPTION - these functions are made to create a fighting game

'''

import random
class Fighter:
    def __init__(self, name):
        self.name = name
        self.hit_points = 10          

    def __repr__(self):
        return self.name + ' (HP: ' + str(self.hit_points) + ')'

    def take_damage(self, damage_amount):
        self.hit_points -= damage_amount

        if self.hit_points <= 0:
            print('\tAlas, ' + self.name + ' has fallen!')
        else:
            print('\t' + self.name + ' has ' + str(self.hit_points) + ' hit points remaining.')

    def attack(self, other):

        print(self.name + ' attacks ' + other.name + '!')
        randnum = random.randrange(1, 21)    
        if randnum >= 12:
            DamageAmount = random.randrange(1, 7)
            print('\tHits for ' + str(DamageAmount) + ' hit points!')
            other.take_damage(DamageAmount)
        else:
            print('\tMisses!')

    def is_alive(self):
        return self.hit_points > 0

def combat_round(fighter1, fighter2):
    randnum1 = random.randrange(1, 7)     
    randnum2 = random.randrange(1, 7)    

    if randnum1 == randnum2:
        print('Simultaneous!')
        fighter1.attack(fighter2)
        fighter2.attack(fighter1)

    elif randnum1 > randnum2:
        fighter1.attack(fighter2)

        if fighter2.is_alive():
            fighter2.attack(fighter1)

    else:
        fighter2.attack(fighter1)

        if fighter1.is_alive():
            fighter1.attack(fighter2)

def main():

    f1 = Fighter('Death_Mongrel')
    f2 = Fighter('Hurt_then_Pain')

    round = 1

    while f1.is_alive() and f2.is_alive():
        print('\n' + (' ROUND ' + str(round) + ' ').center(47, '='))
        print(f1)
        print(f2)

        input('Enter to Fight!')
        combat_round(f1, f2)
        round += 1

    print('\nThe battle is over!')
    print(f1)
    print(f2)

if __name__ == '__main__':
    main()