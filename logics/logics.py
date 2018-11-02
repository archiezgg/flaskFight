from dice import *


def getstatus(barbarian, mage):
    barbarian.get_status()
    print("")
    mage.get_status()
    print("")


def one_round(barbarian, mage):
    who_starts = roll_custom(2)
    if who_starts == 1:
        barbarian.act(mage)
        mage.act(barbarian)
    else:
        mage.act(barbarian)
        barbarian.act(mage)


def get_hp(barbarian, mage):
    print("%s: %d HP left." % (barbarian.name, barbarian.health_point))
    print("%s: %d HP left.\n" % (mage.name, mage.health_point))
