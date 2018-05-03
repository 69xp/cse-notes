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
Skeleton1 = Character('CAPTAIN lowertain', 'A skeleton with some armor, creaking along slowly', 1,
                      ['Stone Rapier', "Iron Helm", 'Stone Boots', 'Rusty Light Armor', 'Iron Chausses'], 1, 1)
Skeleton2 = Character('Skelton C. Bones', 'A half-petrified skeleton, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton3 = Character('Skelton D. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton4 = Character('Skelton E. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton5 = Character('Skelton F. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton6 = Character('Skelton G. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton7 = Character('Skelton H. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton8 = Character('Skelton I. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Necromancer = Character('Lebn Fundi Toyte', '', 8, ["Stygian Bone Steel Longsword"], 3, 4)
Dragon = Character('Bone Dragon', "A ghostly dragon of death", 30, [''], 12, 18)
Leviathan = Character('Cavern Queen', 'A slumbering serpent of the sky, trapped in the depths', 45, [''], 20, 25)


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
parklot1 = Room('Abandoned Lot1',
                'There are several rusted metal objects around you. One of the objects doors is opened'
                'with a strange pale-green light coming through the windshield '
                'that disappears as you walk forward', 'frontgate1', None, None, 'hallway1', None, 'gym', None,
                None,)
gym = Room('Gymnasium', 'you are looking at a large, dimly lit room. it is ahrd to see anything here',
           None, 'parklot1', 'janitorcloset', 'basket_ball_courts', 'lockerroom', 'lockerroom', None, None)
hallway1 = Room('Hallway', 'A hallway that has a passageway to the east and west. '
                           'It appears to continue further south.', 'parklot1', None, None, 'hallway2', None, None,
                "room23", "gym")
room23 = Room('Room23', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'room22', 'hallway1')
room22 = Room('Room22', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'room21', 'room23')
room21 = Room('Room21', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'the_quad', 'room22')
hallway2 = Room('Hallway', 'A hallway that has a passageway to the east and west. '
                           'It appears to continue further south.', 'hallway1', None, None, 'hallway3', None, None,
                "room20", "basket_ball_courts")
room20 = Room('Room20', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'the_quad', 'room19')
room19 = Room('Room19', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'kitchen', 'room18')
room18 = Room('Room18', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'kitchen', 'room18')
basket_ball_courts = Room('The Courts of the Sports', 'An apparent training yard for the defenseless', gym, None, None,
                          'track_field', None, None, 'math_hall', 'field1')
field1 = Room('Orchard of Bountifulness', 'A field full of  fruit trees and edible plants.', None, None, None, 'field2',
              None, None, 'basket_ball_courts', None)
math_hall = Room('Hall of Mind-numbers', 'A hall littered with math tools', None, None, None, None, None, None, 'p1',
                 'basket_ball_courts')
p1 = Room('Storehouse1', 'A storehouse filled with interesting dust there are 2 exits.', None, None, None, None,
          None, None, 'p2', 'math_hall')
p2 = Room('Storehouse2', 'A storehouse filled with interesting boxes. there are 2 exits.', None, None, None, None,
          None, None, 'p3', 'p1')
# P3 put guardian character, guarding 3 weapons.
p3 = Room('Storehouse3', 'A storehouse filled with interesting weapons. there are 2 exits.', None, None, None, None,
          None, None, 'p2', 'p4')
# put sleeping Cavern Queen in hall ERROR
p4 = Room('Storehouse4', 'A storehouse filled with interesting weapons. there are 2 exits.', None, None, None, None,
          None, None, 'p3', 'hall_error')
hall_error = Room('Hall_of_Air-or', 'there is a slumbering leviathan right next to you.  you can faintly see a door at '
                                    'the end of the passage.', None, None, None, None, None, None, 'p4', 'throne_room')
throne_room = Room('Throne Room with the Pants of Doom', 'A dimly lit room full of objects for dark sorcery, hence the '
                                                         'dimness, of course', None, None, None, None, None, None,
                   'hall_error', None)
frontgate2 = Room('Frontgate2', 'You are standing in front of a slightly burnished silver gate which appears to be the '
                  'entrance to a castle, which could also be the mysterious yet famed, ACADEMY.', None,
                  None, None, 'parklot2', None, None, 'frontgate3', 'frontgate1')
parklot2 = Room('Abandoned Lot 2', 'the ground is dry and cracked, yet the air smells like it just rained. '
                'There are paths to the north, east, west, and south.', 'frontgate2', None, None, 'library', None, None,
                'parklot3', 'parklot1')
library = Room('Reading Room of the Ancient Texts', 'A room filled with ancient spell-books', 'parklot2', None, None,
               'spell_practitioners_room', None, None, None, None)
spell_practitioners_room = Room('Spell Practitioners Room', 'A room strewn with spell ingredients and blast marks all'
                                                            'over the room', 'library', None, None, None,
                                'theatre_of_stuff', 'the_cave_system1', None, None)
the_cave_system = Room('The Home of The Defender', 'there are several piles of odds and ends, and there appears to be'
                                                   ' an unused _______in the back of the room.', None,
                       'spell_practitioners_room', 'cavern1', None, None, None, None, None)
cavern1 = Room('The_Fourbidden_Tombs_Entrance', 'skeletons and bones litter the corridor', 'Tomb_of_Fyre', None, None,
               'Tomb_Of_Watur', None, 'the_cave_system', 'Tomb_Of_Urth', 'Tomb_Of_Aer',)
Tomb_of_Fyre = Room('Tomb_of_Fyre', 'A room with pits of lava in the floor, and columns of fire making a path.  '
                                    'there are some GAUNTLETS OF FIRE at the end of the path,', None, None, None,
                    'cavern1', None, None, None, None)
Tomb_of_Watur = Room('Tomb_of_Watur', 'A room with pools of water, and a damp mist parting to reveal a path to '
                                      'the AQUA LEGGINGS.', None, None, None, 'cavern1', None, None, None, None)
Tomb_of_Urth = Room('Tomb_of_Urth', '_', None, None, None, 'cavern1', None, None, None, None)
Tomb_of_Aer = Room('Tomb_of_Aer', '___', None, None, None, 'cavern1', None, None, None, None)
theatre_of_stuff = Room('theatre_of_stuff', 'a gladiator pit, filled with bones of the dead', None,
                        'spell_practitioners_room', None, 'mess_hall', None, None, "Double_you_building", None)
mess_hall = Room('cafeteria_land', 'a gym-like room filled with rotting food.', 'theatre_of_stuff', None, None, None,
                 None, None, None, None)
Double_you_building = Room('Double_you_building', 'A magic testing area', None, None, None, None, None, None,
                           'the_button_room', 'clone_room')
frontgate3 = Room('Frontgate3', 'You are standing in front of an engraved golden gate,which appears to be the entrance'
                                ' to a castle, which could also be the mysterious yet famed, ACADEMY.', None, None,
                  None, 'parklot3', None, None, None, 'frontgate2')
parklot3 = Room('Abandoned Lot 3', 'There are about 16 trees in the apparent orchard, and the grass is way overgrown. '
                'There are paths to the north, south, and west', 'frontgate3', None, None, 'abandoned_classroom1',
                None, None, None, 'parklot2')
abandoned_classroom1 = Room('class_101', 'class lOl looks empty, to the naked eye...', 'parklot3', None, None,
                            'abandoned_classroom2', None, None, 'abandoned_classroom3', None)
abandoned_classroom2 = Room('class_102', 'class lO2 looks empty, to the naked eye...', 'abandoned_classroom1', None,
                            None, None, None, None, 'abandoned_classroom4', None)
abandoned_classroom3 = Room('class_103', 'class lO3 looks empty, to the naked eye...', None, None, None,
                            'abandoned_classroom4', None, None, 'abandoned_classroom5', 'abandoned_classroom1')
abandoned_classroom4 = Room('class 104', 'class lO4 looks empty, to the naked eye...', 'abandoned_classroom3', None,
                            None, None, None, None, 'abandoned_classroom6', 'abandoned_classroom2')
abandoned_classroom5 = Room('class_105', 'class lO5 looks empty, to the naked eye...', None, None, None,
                            'abandoned_classroom4', None, None, 'abandoned_classroom5', 'abandoned_classroom1')
abandoned_classroom6 = Room('class_106', 'there is a pedestal with a _______', 'abandoned_classroom5', None, None, None,
                            None, None, None, 'abandoned_classroom4')


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
