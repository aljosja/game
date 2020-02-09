import random
import time

r = random.SystemRandom()


def roll(number_of_dice: int = 1, eyes_of_die: int = 6, random_seed: float = None):
    time.sleep(.042)
    if random_seed is None:
        random_seed = r.random()
    return number_of_dice * eyes_of_die * random_seed


class Dice:
    def __init__(self, die, dice=6):
        self.die = die
        self.dice = dice
        self.diceType = []

    def roll(self, seed):
        pass

    pass


if __name__ == "__main__":
    print("\n=== This Module Contains ==================")
    print("function: roll(number_of_dice:int = 1, eyes_of_die:int = 6, random_seed:float = random.random()")
    print("===========================================")
    print("roll(6,6,0.5):")
    print(roll(6, 6, 0.0123453545))
    print("roll(3,6):")
    print(roll(3, 6))
    print("5 of those rolls")
    for x in range(0, 5):
        print(roll(3, 6))
    print("===========================================\n")
