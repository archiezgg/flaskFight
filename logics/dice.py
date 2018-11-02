import random


def roll_d10():
    return random.randint(1, 10)


def roll_custom(type_of_dice):
    return random.randint(1, int(type_of_dice))