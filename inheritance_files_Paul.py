class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print("You pick up the %s" % self.name)

    def drop(self):
        print('you drop the %s' % self.name)


class Weapon(Item):
    def __init__(self, name, description, def_boost):
        super(Weapon, self).__init__(name, description)


class Melee(Weapon):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(Melee, self).__init__(name, description, atk_boost)


class Ranged(Weapon):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(Ranged, self).__init__(name, description, atk_boost)


class Consumable(Item):
    def __init__(self, name, description, regen):
        super(Consumable, self).__init__(name, description)


class Health_Potion(Consumable):
    def __init__(self, name, description, health_regen):
        super(Health_Potion, self).__init__(name, description, health_regen)


class Armor(Item):
    def __init__(self, name, description, def_boost):
        super(Armor, self).__init__(name, description)


class Footwear(Armor):
    def __init__(self, name, description, def_boost, speed):
        super(Footwear, self).__init__(name, description, def_boost)


class Five_Yard_Socks(Footwear):
    def __init__(self, name, description, def_boost, speed):
        super(Five_Yard_Socks, self).__init__(name, description, def_boost, speed)


class Iron_Adidas(Footwear):
    def __init__(self, name, description, def_boost, speed):
        super(Iron_Adidas, self).__init__(name, description, def_boost, speed)


class Pants(Armor):
    def __init__(self, name, description, def_boost, strength):
        super(Pants, self).__init__(name, description, def_boost)


class Neon_shorts(Pants):
    def __init__(self, name, description, def_boost, strength):
        super(Neon_shorts, self).__init__(name, description, def_boost)


class Iron_Truesers():
class Shirt(Armor):
    def __init__(self, name, description, def_boost, strength):
        super(Shirt, self).__init__(name, description, def_boost)


class Hawaiian(Shirt):
    def __init__(self, name, description, def_boost, strength):
        super(Hawaiian, self).__init__(name, description, def_boost)


class Hat(Armor):
    def __init__(self, name, description, def_boost, intel):
        super(Hat, self).__init__(name, description, def_boost)


class Cape(Armor):
    def __init__(self, name, description, def_boost, distraction):
        super(Cape, self).__init__(name, description, def_boost)


