from barbarian import Barbarian
from mage import Mage
from logics import *

def arena():
    barbarian = Barbarian("Konan")
    mage = Mage("Borne")
    getstatus(barbarian, mage)

    while True:
        one_round(barbarian, mage)
        get_hp(barbarian, mage)

        if barbarian.health_point <= 0:
            print("Ladies and Gentlemen! %s has fallen. Our winnter is: %s" % (barbarian.name, str(mage.name).upper()))
            break
        elif mage.health_point <= 0:
            print("Ladies and Gentlemen! %s has fallen. Our winnter is: %s" % (mage.name, str(barbarian.name).upper()))
            break


if __name__ == '__main__':
    arena()