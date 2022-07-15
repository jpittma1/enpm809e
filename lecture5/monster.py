from multiprocessing.sharedctypes import Value


class Monster(object):
    weapons = ["sword", "axe", "spear"] #class attribute
    
    def __init__(self, name="Monster", hp=100, life=1, weapon=None):
        if weapon is not None:
            if weapon not in self.weapons:
                raise ValueError(f"{weapon} is not a valid weapon")
            else:
                self.weapon = weapon
        # self.weapons = ["sword", "axe", "spear"]    #instance attribute so not-editable by outside world
        self.name = name
        self.hp = hp
        self.life = life
        self.initial_hp = hp
        self.is_alive = True

    def take_damage(self, damage):
        if self.hp > 0:
            self.hp -= damage
            print(f"{self.name} took {damage} damage points")

        if self.hp <= 0:
            self.life -= 1
            if self.life <= 0:
                print(f"{self.name} is dead")
                self.is_alive = False
            else:
                print(f"{self.name} lost a life")
                print(f"Resetting hp")
                self.hp = self.initial_hp

    def is_dead(self):
        return not self.is_alive
    
    def __str__(self):
        return f"Name: {self.name}, Hp: {self.hp}, Life: {self.life}, Weapon: {self.weapon}"
    
    def __eq__(self, other)-> bool:
        return self.name == other.name
    
    def __le__(self, other) -> bool:
        return self.hp <= other.hp
    
    def __add__(self, num):
        self.life = self.life + num

    def __gt__(self, other) -> bool:
        return self.hp > other.hp
    
    def __sub__(self, num):
        self.life = self.life - num
    


def main():
    # vlad = Monster("Vlad")
    # frankie = Monster("Frankie")
    
    # print(getattr(vlad, "name", None))
    
    # setattr(vlad, "name", "Nosferatu")
    # print(vlad.name)

###----Added weapon class attribute--_####

    # vlad = Monster("Vlad", weapon="axe")
    # # print(vlad.name, vlad.weapon, vlad.hp, vlad.is_alive, vlad.life)
    
    # if hasattr(vlad, "weapon"):
    #     print(vlad.weapon)
    
    # frankie = Monster("Frankie")
    
    # print(Monster.weapons)
    # vlad.weapons.append("knife")
    # print(Monster.weapons)
    # print(frankie.weapons)
    
    # print(vlad)

    # while not vlad.is_dead():
    #     vlad.take_damage(23)

    # print(getattr(vlad, "name", None))      # Vlad
    # print(getattr(vlad, "faction", None))   # None

    # setattr(vlad, "name", "Nosferatu")
    # print(vlad.name)                        # Nosferatu

    # setattr(vlad, "faction", "Vampire")
    # print(vlad.faction)                     # Vampire

    # if hasattr(vlad, "faction"):
    #     delattr(vlad, "faction")
    #     print(vlad.faction)                 # AttributeError

    # delattr(vlad, "name")
    # print(vlad.name)                        # AttributeError
    # print(frankie.name)                     # Frankie

    # delattr(Monster, "life")
    # print(vlad.life)                        # AttributeError
    # print(frankie.life)                     # AttributeError


    # vlad = Monster("Vlad", weapon="axe")
    # if hasattr(vlad, "weapon"):
    #     print(vlad.weapon)


    ##---Added overrides to eq, add, le, gt---###
    vlad = Monster("Vlad")
    frankie = Monster("Frankie")
    print(f"Vlad life: {vlad.life}")
    vlad + 1
    print(f"Vlad life: {vlad.life}")
    frankie - 2
    print(f"Frankie life: {frankie.life}")
    
    print ("Is Vlad life > Frankie Life? ", vlad > frankie)
    print ("Is Vlad life <= Frankie Life? ", vlad <= frankie)

if __name__ == "__main__":
    main()
