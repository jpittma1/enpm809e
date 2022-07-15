import random


class Weapon():

    def __init__(self, name, weapon_type, power):
        self._name = name
        self._weapon_type = weapon_type
        self._power = power

    @property
    def name(self):
        return self._name

    @property
    def weapon_type(self):
        return self._weapon_type

    @property
    def power(self):
        return self._power

    def power_up(self, power) -> None:
        pass

    def __str__(self):
        return(f"Name: {self._name}, Type: {self._weapon_type}, Power: {self._power}")


def main():
    void_sword = Weapon("The Void Sword", "sword", 2000)
    print(void_sword.name)
    print(void_sword.weapon_type)
    print(void_sword.power)


if __name__ == '__main__':
    main()
