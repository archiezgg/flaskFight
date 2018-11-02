from dice import *


class Mage(object):
    name = ''
    intelligence = 0
    stamina = 0
    health_point = 0
    base_damage = 0

    def __init__(self, name):
        self.name = name
        self.intelligence = roll_d10()
        self.stamina = roll_d10()
        self.health_point = roll_custom(51) + 50 + self.stamina
        self.base_damage = roll_d10() + self.intelligence

    def eat_fire(self):
        self.health_point += self.stamina
        print("%s does something that would seem horrible to a non-pyromaniac person. "
              "He begins to cast fire in his left palm and shoves it into his mouth. "
              "It heals him by %d points." % (self.name, self.stamina))

    def fireball(self, barbarian):
        damage = roll_d10() + self.base_damage
        barbarian.health_point -= damage
        print("%s hurls a fireball at his enemies. It does %d damage" % (self.name, damage))

    def fire_arrow(self, barbarian):
        arrow_count = roll_custom(4)
        damage = self.base_damage + 2 * arrow_count
        barbarian.health_point -= damage
        print("%s shoots %d arrows at his enemy. It does %d damage." % (self.name, arrow_count, damage))

    def fire_wall(self, barbarian):
        damage = roll_d10() + self.base_damage
        barbarian.health_point -= damage
        print("%s creates a fiery firewall between him and his opponent. It does %d damage" % (self.name, damage))

    def act(self, barbarian):
        which_skill = roll_custom(4)

        if which_skill == 1:
            self.eat_fire()
        elif which_skill == 2:
            self.fireball(barbarian)
        elif which_skill == 3:
            self.fire_arrow(barbarian)
        elif which_skill == 4:
            self.fire_wall(barbarian)

    def get_status(self):
        print("%s has the following stats:\n"
              "Intelligence: %d\n"
              "Stamina %d\n"
              "Base damage: %d\n"
              "HP: %d" % (self.name, self.intelligence, self.stamina, self.base_damage, self.health_point))
