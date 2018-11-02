from barbarian import Barbarian
from mage import Mage
from logics import *

def fight(barbarian, mage):
    console_log = ''
    console_log += getstatus(barbarian, mage) + '\n'

    while True:
        console_log += one_round(barbarian, mage) + '\n'
        console_log += get_hp(barbarian, mage) + '\n'

        if barbarian.health_point <= 0:
            console_log += "Ladies and Gentlemen! %s has fallen. Our winnter is: %s" % (barbarian.name, str(mage.name).upper())
            break
        elif mage.health_point <= 0:
            console_log += "Ladies and Gentlemen! %s has fallen. Our winnter is: %s" % (mage.name, str(barbarian.name).upper())
            break

    return console_log
