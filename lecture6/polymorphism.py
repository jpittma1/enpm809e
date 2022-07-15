class Vampire:
    def __init__(self, name):
        self._name = name

    def attack(self):
        print(f"{self._name} attacks")


class Skeleton:
    def __init__(self, name):
        self._name = name

    def attack(self):
        print(f"{self._name} attacks")


def main():
    vampire = Vampire("Drake")
    skeleton = Skeleton("Skeletor")
    for monster in (vampire, skeleton):
        monster.attack()


if __name__ == "__main__":
    main()
