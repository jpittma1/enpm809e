
from monster import Monster
from weapon import Weapon

class Vampire(Monster):
    def __init__(self, name="monster", hp=50, life=3):
        self._name = name
        self._hp = hp
        self._life = life
        self._initial_hp = hp
        self._is_alive = True
        self._dodge_chance = 4
        self._weapon = Weapon(None, None, None)

    def __str__(self):
        return f'Vampire\'s Name: {self._name}, HP: {self._hp}, Life: {self._life}, Weapon: {self._weapon}'

    @property
    def _dodge(self):
        #return True if dodges, False if doesn't
        if self._dodge_chance > 2:
            return True
        else:
            return False
        # return self._dodge_chance

    def take_damage(self, damage):
        if self._dodge == False:
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
        
        else:
            print(f"{self._name} dodged the attack and has {self._hp} hp left")

    
