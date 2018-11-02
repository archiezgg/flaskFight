class Weapon(object):
    weapon_damage = 5
    self_heal = 0
    self_damage = 0

    def __init__(self, is_enchanted, is_cursed):
        if is_enchanted:
            self.weapon_damage += 5
            self.self_heal = 5

        if is_cursed:
            self.weapon_damage += 5
            self.self_damage = 10
