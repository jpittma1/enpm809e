
# ---------------
# #  VERSION 1.0
# ---------------

# class Monster:
#     def __init__(self, name="Monster", hp=100, life=1):
#         self.name = name
#         self.hp = hp
#         self.life = life
#         self.initial_hp = hp
#         self.is_alive = True

#     def __str__(self):
#         return f'Name: {self.name}, HP: {self.hp}, Life: {self.life}'

#     def take_damage(self, damage):
#         if self.hp > 0:
#             self.hp -= damage
#             print(f"{self.name} took {damage} damage points")

#         if self.hp <= 0:
#             self.life -= 1
#             if self.life <= 0:
#                 print(f"{self.name} is dead")
#                 self.is_alive = False
#             else:
#                 print(f"{self.name} lost a life")
#                 print(f"Resetting hp")
#                 self.hp = self.initial_hp

#     def is_dead(self):
#         return not self.is_alive

#     def __add__(self, num):
#         self.life = self.life + num

#     def __gt__(self, other):
#         return self.hp > other.hp


# def main():
#     vlad = Monster("Vlad")
#     print(vlad.hp)
#     vlad.hp = -10


# if __name__ == "__main__":
#     main()


# ---------------
# #  VERSION 2.0
# ---------------

# class Monster:
#     def __init__(self, name="Monster", hp=100, life=1):
#         self._name = name
#         self._hp = hp
#         self._life = life
#         self._initial_hp = hp
#         self._is_alive = True

#     def __str__(self):
#         return f'Name: {self._name}, HP: {self._hp}, Life: {self._life}'

#     def get_hp(self):
#         return self._hp

#     def take_damage(self, damage):
#         if self._hp > 0:
#             self._hp -= damage
#             print(f"{self.name} took {damage} damage points")

#         if self._hp <= 0:
#             self._life -= 1
#             if self._life <= 0:
#                 print(f"{self.name} is dead")
#                 self._is_alive = False
#             else:
#                 print(f"{self.name} lost a life")
#                 print(f"Resetting hp")
#                 self._hp = self.initial_hp

#     def is_dead(self):
#         return not self._is_alive

#     def __add__(self, num):
#         self._life = self._life + num

#     def __gt__(self, other):
#         return self._hp > other.hp


# def main():
#     vlad = Monster("Vlad")
#     print(vlad.get_hp())
#     vlad._hp = -10


# if __name__ == "__main__":
#     main()


# ---------------
# #  VERSION 3.0
# ---------------

# class Monster:
#     def __init__(self, name="Monster", hp=100, life=1):
#         self._name = name
#         self._hp = hp
#         self._life = life
#         self._initial_hp = hp
#         self._is_alive = True

#     def __str__(self):
#         return f'Name: {self._name}, HP: {self._hp}, Life: {self._life}'

#     def _get_name(self):
#         return self._name

#     def _set_name(self, name):
#         self._name = name

#     def _get_hp(self):
#         return self._hp

#     def take_damage(self, damage):
#         if self._hp > 0:
#             self._hp -= damage
#             print(f"{self._name} took {damage} damage points")

#         if self._hp <= 0:
#             self._life -= 1
#             if self._life <= 0:
#                 print(f"{self._name} is dead")
#                 self._is_alive = False
#             else:
#                 print(f"{self._name} lost a life")
#                 print(f"Resetting hp")
#                 self._hp = self._initial_hp

#     def _is_dead(self):
#         return not self._is_alive

#     # name = property(fget=None, fset=_set_name)
#     name = property(_get_name, _set_name)
#     hp = property(_get_hp)


# def main():
#     vlad = Monster("Vlad")
#     print(vlad.name)
#     vlad.name = "Drake"
#     print(vlad.hp)
#     # vlad.hp = -10


# if __name__ == "__main__":
#     main()

# ---------------
# #  VERSION 4.0
# ---------------

# from abc import ABC, abstractmethod
# from weapon import Weapon


# class Monster():
#     def __init__(self, name="Monster", hp=100, life=1):
#         self._name = name
#         self._hp = hp
#         self._life = life
#         self._initial_hp = hp
#         self._is_alive = True

#     def __str__(self):
#         return f'Name: {self._name}, HP: {self._hp}, Life: {self._life}'

#     @property
#     def name(self):
#         return self._name
#         # raise Exception("You cannot get the name")

#     @name.setter
#     def name(self, name):
#         self._name = name

#     @property
#     def hp(self):
#         return self._hp

#     @property
#     def is_alive(self):
#         return self._is_alive

#     @property
#     def life(self):
#         return self._life

#     def take_damage(self, damage):
#         if self._hp > 0:
#             self._hp -= damage
#             print(f"{self._name} took {damage} damage points")
#             print(f"{self._name} has {self._hp} hp left")

#         if self._hp <= 0:
#             self._life -= 1
#             if self._life <= 0:
#                 print(f"{self._name} is dead")
#                 self._is_alive = False
#             else:
#                 print(f"{self._name} lost a life")
#                 print(f"Resetting hp")
#                 self._hp = self._initial_hp

#     def _is_dead(self):
#         pass
#         return not self._is_alive


# def main():
#     vlad = Monster()
#     print(vlad.name)
#     vlad.name = "Drake"
#     print(vlad.name)
#     print(f"vlad.hp is {vlad.hp}")
#     # vlad.hp = -10

# if __name__ == "__main__":
#     main()


# The Object Superclass

class MyClass:
    pass


def main():
    my_class = MyClass()
    my_object = object()
    print(dir(my_class))   # list all members in MyClass
    print()
    print(dir(my_object))  # list all members in object class


if __name__ == "__main__":
    main()
