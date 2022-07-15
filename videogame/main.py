from monster import Monster
from vampire import Vampire
from werewolf import Werewolf
from weapon import Weapon



def main():
    drake = Monster("Drake")
    vlad = Vampire("Vlad")
    hairy = Werewolf("Hairy")
    # print(vlad.name)
    # drake.name = "Drake"
    # vlad.name = "Vlad"
    # hairy.name = "Hairy"
    # print(f"vlad.hp is {vlad.hp}")
    print (drake)
    print (vlad)
    print (hairy)
    # vlad.hp = -10

if __name__ == "__main__":
    main()