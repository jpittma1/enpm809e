from monster import Monster
from weapon import Weapon

class Werewolf(Monster):
    def __init__(self, name="monster", hp=200, life=1):
        self._name = name
        self._hp = hp
        self._life = life
        self._initial_hp = hp
        self._is_alive = True
        self._strength = 3
        self._weapon = Weapon(None, None, None)

    def __str__(self):
        return f'Werewolf\'s Name: {self._name}, HP: {self._hp}, Life: {self._life}, Weapon: {self._weapon}'

    def take_damage(self, damage):
        #reduce damage tacken based on strength
        if self._hp > 0:
            self._hp -= (damage - self._strength)
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
    
    @property
    def strength(self):
        return self._strength