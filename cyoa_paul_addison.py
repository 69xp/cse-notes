import random


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print("You pick up the %s" % self.name)

    def drop(self):
        print('you drop the %s' % self.name)


class Weapon(Item):
    def __init__(self, name, description, atk_boost):
        super(Weapon, self).__init__(name, description)
        self.atk_boost = atk_boost


class Melee(Weapon):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(Melee, self).__init__(name, description, atk_boost)
        self.speed = speed
        self.damage_infliction = damage_infliction
        self.atk_boost = atk_boost


class BoneClub(Melee):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(BoneClub, self).__init__(name, description, atk_boost, speed, damage_infliction)
        self.speed = 1
        self.damage_infliction = 4
        self.atk_boost = 1


class ButterKnife(Melee):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(ButterKnife, self).__init__(name, description, atk_boost, speed, damage_infliction)
        self.speed = 1
        self.damage_infliction = 2
        self.atk_boost = 1


class PlasticGladius(Melee):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(PlasticGladius, self).__init__(name, description, atk_boost, speed, damage_infliction)
        self.speed = 1
        self.damage_infliction = 4
        self.atk_boost = 6


class StygianBoneSteelLongsword(Melee):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(StygianBoneSteelLongsword, self).__init__(name, description, atk_boost, speed, damage_infliction)
        self.speed = 2
        self.damage_infliction = 5
        self.atk_boost = 6


class Ranged(Weapon):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(Ranged, self).__init__(name, description, atk_boost)
        self.speed = speed
        self.damage_infliction = damage_infliction
        self.atk_boost = atk_boost


class BoomcornLauncher(Ranged):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(BoomcornLauncher, self).__init__(name, description, atk_boost, speed, damage_infliction)
        self.atk_boost = 4
        self.damage_infliction = 2
        self.speed = 3


class Consumable(Item):
    def __init__(self, name, description, regen):
        super(Consumable, self).__init__(name, description)
        self.regen = regen


class Pizza(Consumable):
    def __init__(self, name, description, regen):
        super(Pizza, self).__init__(name, description, regen)
        self.regen = 3


class Potion(Consumable):
    def __init__(self, name, description, regen):
        super(Potion, self).__init__(name, description, regen)
        self.regen = 5


class TheoreticallyEatenSandwich(Consumable):
    def __init__(self, name, description, regen):
        super(TheoreticallyEatenSandwich, self).__init__(name, description, regen)
        self.regen = 3


class Armor(Item):
    def __init__(self, name, description, def_boost):
        super(Armor, self).__init__(name, description)
        self.def_boost = def_boost


class Footwear(Armor):
    def __init__(self, name, description, def_boost, speed):
        super(Footwear, self).__init__(name, description, def_boost)
        self.def_boost = def_boost
        self.speed = speed


class FiveYardSocks(Footwear):
    def __init__(self, name, description, def_boost, speed):
        super(FiveYardSocks, self).__init__(name, description, def_boost, speed)
        self.speed = 4
        self.def_boost = 1


class StoneBoots(Footwear):
    def __init__(self, name, description, def_boost, speed):
        super(StoneBoots, self).__init__(name, description, def_boost, speed)
        self.speed = 0
        self.def_boost = 4


class IronAdidas(Footwear):
    def __init__(self, name, description, def_boost, speed):
        super(IronAdidas, self).__init__(name, description, def_boost, speed)
        self.def_boost = 3
        self.speed = 1


class Pants(Armor):
    def __init__(self, name, description, def_boost, strength):
        super(Pants, self).__init__(name, description, def_boost)
        self.def_boost = def_boost
        self.strength = strength


class NeonShorts(Pants):
    def __init__(self, name, description, def_boost, strength):
        super(NeonShorts, self).__init__(name, description, def_boost, strength)
        self.def_boost = 2
        self.strength = 2


class IronTrousers(Pants):
    def __init__(self, name, description, def_boost, strength):
        super(IronTrousers, self).__init__(name, description, def_boost, strength)
        self.def_boost = 4
        self.strength = 3


class IronChausses(Pants):
    def __init__(self, name, description, def_boost, strength):
        super(IronChausses, self).__init__(name, description, def_boost, strength)
        self.def_boost = 4
        self.strength = 3


class Shirt(Armor):
    def __init__(self, name, description, def_boost, strength):
        super(Shirt, self).__init__(name, description, def_boost)
        self.def_boost = def_boost
        self.strength = strength


class Hawaiian(Shirt):
    def __init__(self, name, description, def_boost, strength):
        super(Hawaiian, self).__init__(name, description, def_boost, strength)
        self.def_boost = 3
        self.strength = 0


class IronUpperBodyPlate(Shirt):
    def __init__(self, name, description, def_boost, strength):
        super(IronUpperBodyPlate, self).__init__(name, description, def_boost, strength)
        self.def_boost = 5
        self.strength = 3


class RustyLightArmor(Shirt):
    def __init__(self, name, description, def_boost, strength):
        super(RustyLightArmor, self).__init__(name, description, def_boost, strength)
        self.def_boost = 2
        self.strength = 2


class Hat(Armor):
    def __init__(self, name, description, def_boost, conf):
        super(Hat, self).__init__(name, description, def_boost)
        self.def_boost = def_boost
        self.conf = conf


class IronHelm(Hat):
    def __init__(self, name, description, def_boost, conf):
        super(IronHelm, self).__init__(name, description, def_boost, conf)
        self.def_boost = 3
        self.conf = 2


class PropellerHat(Hat):
    def __init__(self, name, description, def_boost, conf):
        super(PropellerHat, self).__init__(name, description, def_boost, conf)
        self.def_boost = 0
        self.conf = 3
        self.speed = 2


class Cape(Armor):
    def __init__(self, name, description, def_boost, distraction):
        super(Cape, self).__init__(name, description, def_boost)
        self.distraction = distraction


class AestheticCape(Cape):
    def __init__(self, name, description, def_boost, distraction):
        super(AestheticCape, self).__init__(name, description, def_boost, distraction)
        self.distraction = 3


class ShinyCape(Cape):
    def __init__(self, name, description, def_boost, distraction):
        super(ShinyCape, self).__init__(name, description, def_boost, distraction)
        self.distraction = 5


class Character(object):
    def __init__(self, name, description, health, items, atk, defense):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = items
        self.dmg = atk
        self.defense = defense
        self.death = False

    def attack(self, opponent):
        attack = random.randint(1, 3)
        damage = random.randint(0, self.dmg)
        if attack == 1:
            print('%s hits %s!' % (self.name, opponent.name))
            opponent.health -= damage
        if attack == 2:
            print('%s missed %s!' % (self.name, opponent.name))

        if attack == 3:
            print('%s hits %s!' % (opponent.name, self.name))
            self.health -= damage

    def take_damage(self):
        self.health -= 1

    def death(self):
        if self.take_damage >= self.health:
            if self.health == 0:
                self.death = True
                print('%s is dead...' % self.name)


HERO = Character('Randomly Generic Name', 'A blank slate', 6, ['butter knife'], 3, 3)
Ogre = Character('Yo-Ogre-Urt', 'like a cyclops only with two eyes.', 5, ['bone club'], 4, 2)
Skeleton1 = Character('Skelton B. Bones', 'A half-petrified skeleton, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton2 = Character('Skelton C. Bones', 'A skeleton with armor, creaking along slowly', 1,
                      ['Stone Rapier', "Iron Helm", 'Stone Boots', 'Rusty Light Armor', 'Iron Chausses'], 1, 1)
Skeleton3 = Character('Skelton D. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Necromancer = Character('Lebn Fundi Toyte', '', 8, ["Stygian Bone Steel Longsword"], 3, 4)
Dragon = Character('Bone Dragon', "A ghostly dragon of death", 30, [''], 12, 18)


class Room(object):
    def __init__(self, name, description, north, northeast, northwest, south, southeast, southwest, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.name = name
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


bland_room = Room("Bland Room", 'There are three portals, one to the north, east, and west. Each is a different color.',
                  'frontgate1', None, None, None, None, None, 'frontgate2', 'frontgate3')
frontgate1 = Room('Frontgate1', 'You are in front of a rusted iron gate which appears to be the entrance to a castle, '
                  'which could also be the mysterious yet famed, ACADEMY.',
                  None, None, None, 'parkinglot1', None, 'gym', 'frontgate2', None)
frontgate2 = Room('Frontgate2', 'You are standing in front of a slightly burnished silver gate which appears to be the '
                  'entrance to a castle, which could also be the mysterious yet famed, ACADEMY.', None,
                  None, None, 'parklot2', None, None, 'frontgate3', 'frontgate1')
frontgate3 = Room('Frontgate3', 'You are standing in front of an engraved golden gate,which appears to be the entrance'
                  ' to a castle, which could also be the mysterious yet famed, ACADEMY.', None, None, None, 'parklot3',
                  None, None, None, 'frontgate2')
parklot1 = Room('Abandoned Lot1',
                'There are several rusted metal objects around you. One of the objects doors is opened'
                'with a strange pale-green light coming through the windshield '
                'that disappears as you walk forward', 'frontgate1', None, None, 'hallway1', None, 'gym', None,
                None,)
parklot2 = Room('Abandoned Lot 2', 'the ground is dry and cracked, yet the sky looks dark and stormy. '
                'There are paths to the north, east, west, and south.', 'frontgate2', None, None, 'library', None, None,
                'parkinglot3', 'parkinglot1')
parklot3 = Room('Abandoned Lot 3', 'There are about 16 trees in the apparent orchard, and the grass is way overgrown. '
                'There are paths to the north, south, and west', 'frontgate3', None, None, 'abandoned_classroom1', None,
                None, None, 'parklot2')
gym = Room('Gymnasium', 'you are looking at a large, dimly lit room. it is ahrd to see anything here',
           None, 'parklot1', 'janitorcloset', None, 'lockerroom', 'lockerroom', None, None)
hallway1 = Room('Hallway', 'A hallway that has a passageway to the east and west. '
                           'It appears to continue further south.', 'parklot1', None, None, 'hallway2', None, None,
                "room23", "gym")
room23 = Room('Room23', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'room22', 'hallway1')
room22 = Room('Room23', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'room23', 'room21')


current_node = bland_room
directions = ['north', 'northwest', 'west', 'southwest', 'south', 'southeast', 'east', 'northeast']
short_directions = ['n', 'nw', 'w', 'sw', 's', 'se', 'e', 'ne']


while True:
    # Prints the current node
    print(current_node.name)
    print(current_node.description)

    # Takes what you put in
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)

    # Redefines the command to a new direction
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Movement
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You should not, will not, and cannot go this way!')
    elif command[:7] == 'pick up':
        item = command[8:]
    else:
        print('Command not recognized')
