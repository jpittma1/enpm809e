
# ---------------
# #  VERSION 4.0
# ---------------

from abc import ABC, abstractmethod

# from werewolf import Werewolf
# from vampire import Vampire
from weapon import Weapon


class Monster():
    def __init__(self, name="Monster", hp=100, life=1):
        self._name = name
        self._hp = hp
        self._life = life
        self._initial_hp = hp
        self._is_alive = True
        self._weapon = Weapon(None, None, None)
        
        # weapon = Weapon(weapon) #'name', 'weapon_type', and 'power'
        
    def __str__(self):
        return f'Name: {self._name}, HP: {self._hp}, Life: {self._life}, Weapon: {self._weapon}'

    @property
    def name(self):
        return self._name
        # raise Exception("You cannot get the name")

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def life(self):
        return self._life

    def take_damage(self, damage):
        if self._hp > 0:
            self._hp -= damage
            print(f"{self._name} took {damage} damage points")
            print(f"{self._name} has {self._hp} hp left")

        if self._hp <= 0:
            self._life -= 1
            if self._life <= 0:
                print(f"{self._name} is dead")
                self._is_alive = False
            else:
                print(f"{self._name} lost a life")
                print(f"Resetting hp")
                self._hp = self._initial_hp

    def _is_dead(self):
        pass
        return not self._is_alive
    
    @property
    def weapon(self):
        return self._weapon


def main():
    drake = Monster("Drake")
    # vlad = Vampire("Vlad")
    # hairy = Werewolf("Hairy")
    # print(vlad.name)
    # drake.name = "Drake"
    # vlad.name = "Vlad"
    # hairy.name = "Hairy"
    # print(f"vlad.hp is {vlad.hp}")
    print (drake)
    # print (vlad)
    # print (hairy)
    # vlad.hp = -10

if __name__ == "__main__":
    main()



