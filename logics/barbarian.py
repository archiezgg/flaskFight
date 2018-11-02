from dice import *
from weapon import Weapon


class Barbarian(object):
    name = ''
    strength = roll_d10()
    stamina = roll_d10()
    health_point = roll_custom(51) + 50 + stamina
    base_damage = roll_d10() + strength

    def __init__(self, name):
        self.name = name

    def battle_cry(self):
        heal = roll_d10() + self.stamina
        self.health_point += heal
        print('%s has just used BattleCry, and healed %d hp. He has %d hp left.' % (self.name, heal, self.health_point))

    def use_weapon(self, mage):
        sword = Weapon(True, False)
        axe = Weapon(False, True)
        hammer = Weapon(True, True)

        which_weapon = roll_custom(3)

        if which_weapon == 1:
            damage = sword.weapon_damage + self.base_damage
            self.health_point += sword.self_heal
            self.health_point -= sword.self_damage
            mage.health_point -= damage
            print("%s used his Enchanted Sword, and caused %d damage on %s and healed %d on himself." % (
                self.name, damage, mage.name, sword.self_heal))
        elif which_weapon == 2:
            damage = axe.weapon_damage + self.base_damage
            self.health_point += axe.self_heal
            self.health_point -= axe.self_damage
            mage.health_point -= damage
            print("%s used his Cursed Axe, and caused %d damage on %s and damaged %d on himself." % (
                self.name, damage, mage.name, axe.self_damage))
        else:
            damage = hammer.weapon_damage + self.base_damage
            self.health_point += hammer.self_heal
            self.health_point -= hammer.self_damage
            mage.health_point -= damage
            print("%s used his Hammer of Absolute Destruction, and caused %d damage on %s and %d/%d on himself." % (
                self.name, damage, mage.name, hammer.self_heal, hammer.self_damage))

    def act(self, mage):
        which_skill = roll_custom(2)

        if which_skill == 1:
            self.battle_cry()
        else:
            self.use_weapon(mage)

    def get_status(self):
        print("%s has the following stats:\n"
              "Strength: %d\n"
              "Stamina %d\n"
              "Base damage: %d\n"
              "HP: %d" % (self.name, self.strength, self.stamina, self.base_damage, self.health_point))
