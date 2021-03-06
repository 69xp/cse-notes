import random
inventory = []


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def steal(self):
        print("You took the %s" % self.name)

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


class Ranged(Weapon):
    def __init__(self, name, description, atk_boost, speed, damage_infliction):
        super(Ranged, self).__init__(name, description, atk_boost)
        self.speed = speed
        self.damage_infliction = damage_infliction
        self.atk_boost = atk_boost


class Consumable(Item):
    def __init__(self, name, description, regen):
        super(Consumable, self).__init__(name, description)
        self.regen = regen


class Potion(Consumable):
    def __init__(self, name, description, regen):
        super(Potion, self).__init__(name, description, regen)
        self.regen = 5


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


class ShatterersShielding(Cape):
    def __init__(self, name, description, def_boost, distraction):
        super(ShatterersShielding, self).__init__(name, description, def_boost, distraction)
        self.distraction = 5
        self.def_boost = 6


BoneClub = Melee('Bone Club', 'A large club made from what looks like a femur', 1, 1, 4)
ButterKnife = Melee('Butter Knife', 'A blade forged for butter most spreadable', 1, 1, 2)
PlasticGladius = Melee('Plastic Gladius', 'A short sword composed of plasticite', 4, 4, 1)
StickianBoneSteelLongsword = Melee('Stickian Bone Steel Longsword', 'A longsword forged with superheated carbon from '
                                                                    'the bones of your enemies, '
                                                                    'and cooled in the River Sticks', 6, 2, 5)
CattleAxe = Melee('Cattle Axe', 'A mechanized axe with the force of a hundred raging bulls', 9, 1, 8)
IonWielder = Melee('IonWielder', 'A beautifully crafted sword, made from Glorium', 10, 2, 12)
BoomcornLauncher = Ranged('Boomcorn Launcher', 'A crossbow-esque mechanism, that fires explosive popcorn kernels', 4, 3,
                          2)
MagicShuriken = Ranged('A Magical Shuriken', 'A magic throwing star', 2, 5, 3)
RazoredgeArchbow = Ranged('Razoredge Archbow', 'A recurve bow of tremendous power, with stabby blades all over it', 5,
                          9, 7)
PizzaBurg = Consumable('Double-decker Pizza Burger', 'Two pizzas inside two burgers, in between two pizzas', 6)
TheoreticallyEatenSandwich = Consumable('TheoreticallyEatenSandwich', 'A sandwich that has been theoretically eaten', 9)


class Character(object):
    def __init__(self, name, description, health, items, atk, defense):
        self.name = name
        self.description = description
        self.health = health
        self.dmg = atk
        self.defense = defense
        self.death = False
        self.items = items

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

    def steal(self):
        Item.steal(self.name)


HERO = Character('Randomly Generic Name', 'A blank slate', 6, [ButterKnife], 3, 3)
Ogre = Character('Yo-Ogre-Urt', 'like a cyclops only with two eyes, and made of yo-gurt', 5, [BoneClub], 4, 2)
Skeleton1 = Character('Skelton B. Bones', 'A skeleton with some armor, creaking along slowly', 1,
                      ['Stone Rapier', "Iron Helm", 'Stone Boots', 'Rusty Light Armor', 'Iron Chausses'], 1, 1)
Skeleton2 = Character('Skelton C. Bones', 'A half-petrified skeleton, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton3 = Character('Skelton D. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton4 = Character('Skelton E. Bones', 'A skeleton, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton5 = Character('Skelton F. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton6 = Character('Skelton G. Bones', 'A skeleton with three arms, creaking along slowly', 1, ['Stone Rapier'], 1,
                      1)
Skeleton7 = Character('Skelton H. Bones', 'A skeleton with no arms, creeping along slowly', 1, [''], 1, 1)
Skeleton8 = Character('Skelton I. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Necromancer = Character('Lebn Fundi Toyte', '', 8, [StickianBoneSteelLongsword], 3, 4)
Dragon = Character('Bone Dragon', "A ghostly dragon of death", 30, [''], 12, 18)
Leviathan = Character('Cavern Queen', 'A slumbering serpent of the sky, trapped in the depths', 45, [''], 20, 25)
SportsTroll = Character('Gym Creacher', 'a huge troll made out of sports equipment', 12, ['HockeySword'], 13, 14)
Minitar = Character('Minitar', 'A small bull made out of tar standing upright, wielding a battle axe.', 6,
                    [CattleAxe], 6, 6)
Gourdian_of_the_Squash = Character('Gourdian of the Sa-Squash', 'A towering figure made from different gourds and '
                                                                'squashes', 8, None, 10, 5)


class Room(object):
    def __init__(self, name, description, north, northeast, northwest, south, southeast, southwest, east, west,
                 characters, objects):
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
        self.characters = characters
        self.objects = objects

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


bland_room = Room("Bland Room", 'There are three portals, one to the north, east, and west. Each is a different color.',
                  'frontgate1', None, None, None, None, None, 'frontgate2', 'frontgate3', None, None)
frontgate1 = Room('Frontgate1', 'You are in front of a rusted iron gate which appears to be the entrance to a castle, '
                  'which could also be the mysterious yet famed, ACADEMY.',
                  None, None, None, 'parkinglot1', None, 'gym', 'frontgate2', None, None, None,)
parklot1 = Room('Abandoned Lot1',
                'There are several rusted metal objects around you. One of the objects doors is opened'
                'with a strange pale-green light coming through the windshield that disappears as you walk forward',
                'frontgate1', None, None, 'hallway1', None, 'gym', None,
                None, None, ['TheoreticallyEatenSandwich'])
gym = Room('Gymnasium', 'you are looking at a large, dimly lit room. it is hard to see anything here',
           None, 'parklot1', 'janitorcloset', 'basket_ball_courts', 'Flockerroom', 'Mlockerroom', None, None,
           [SportsTroll], None,)
Flockerroom = Room('sorceresses dressing room', 'A tidily organized room', None, None, 'gym', None, None, None, None,
                   None, None, None, )
Mlockerroom = Room('sorcerers dressing room', 'A room stuffed with articles of clothing, with a shiny cape or two',
                   None, 'gym', None, None, None, None, None, None, None, [MagicShuriken, ShinyCape])
janitorcloset = Room('Janitor Closet', 'lol', None, None, None, None, None, 'gym', None, None, None, [
                     'Dadao of Cleanliness'], )
hallway1 = Room('Hallway', 'A hallway that has a passageway to the east and west.'
                           'It appears to continue further south.', 'parklot1', None, None, 'hallway2', None, None,
                "room23", "gym", None, None,)
room23 = Room('Room23', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'room22', 'hallway1', None, None,)
room22 = Room('Room22', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'room21', 'room23', None, None,)

room21 = Room('Room21', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'the_quad', 'room22', ['Minitar'], None,)
hallway2 = Room('Hallway', 'A hallway that has a passageway to the east and west. '
                           'It appears to continue further south.', 'hallway1', None, None, 'hallway3', None, None,
                "room20", "basket_ball_courts", None, None,)
room20 = Room('Room20', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'the_quad', 'room19', None, None,)
room19 = Room('Room19', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'kitchen', 'room18', None, ['Shardsaber', 'Shatterers Shielding'],)
room18 = Room('Room18', 'the only entrance is the one you just came through, however there is an exit to the east',
              None, None, None, None, None, None, 'kitchen', 'room18', None, None,)
basket_ball_courts = Room('The Courts of the Sports', 'An apparent training yard for the defenseless', gym, None, None,
                          'track_field', None, None, 'math_hall', 'field1', None, None,)
field1 = Room('Orchard of Bountifulness', 'A field full of  fruit trees and edible plants.', None, None, None, 'field2',
              None, None, 'basket_ball_courts', None, None, None,)
math_hall = Room('Hall of Mind-numbers', 'A hall littered with math tools', None, None, None, None, None, None, 'p1',
                 'basket_ball_courts', None, None,)
p1 = Room('Storehouse1', 'A storehouse filled with interesting dust there are 2 exits.', None, None, None, None,
          None, None, 'p2', 'math_hall', None, None,)
p2 = Room('Storehouse2', 'A storehouse filled with interesting boxes. there are 2 exits.', None, None, None, None,
          None, None, 'p3', 'p1', None, None,)
# P3 put guardian character, guarding 3 weapons.
p3 = Room('Storehouse3', 'A storehouse filled with interesting weapons. there are 2 exits.', None, None, None, None,
          None, None, 'p2', 'p4', None, ['IonWielder', 'RazoredgeArchbow', ],)
# put sleeping Cavern Queen in hall ERROR
p4 = Room('Storehouse4', 'A storehouse filled with interesting weapons. there are 2 exits.', None, None, None, None,
          None, None, 'p3', 'hall_error', ['Leviathan', ], None,)
hall_error = Room('Hall_of_Air-or', 'there is a slumbering leviathan right next to you.  you can faintly see a door at '
                                    'the end of the passage.', None, None, None, None, None, None, 'p4', 'throne_room',
                  ['Leviathan'], None,)
throne_room = Room('Throne Room with the Pants of Doom', 'A dimly lit room full of objects for dark sorcery, hence the '
                                                         'dimness, of course', None, None, None, None, None, None,
                   'hall_error', None, None, None,)
frontgate2 = Room('Frontgate2', 'You are standing in front of a slightly burnished silver gate which appears to be the '
                  'entrance to a castle, which could also be the mysterious yet famed, ACADEMY.', None,
                  None, None, 'parklot2', None, None, 'frontgate3', 'frontgate1', None, None,)
parklot2 = Room('Abandoned Lot 2', 'the ground is dry and cracked, yet the air smells like it just rained. '
                'There are paths to the north, east, west, and south.', 'frontgate2', None, None, 'library', None, None,
                'parklot3', 'parklot1', None, None,)
library = Room('Reading Room of the Ancient Texts', 'A room filled with ancient spell-books', 'parklot2', None, None,
               'spell_practitioners_room', None, None, None, None, None, None,)
spell_practitioners_room = Room('Spell Practitioners Room', 'A room strewn with spell ingredients and blast marks all'
                                                            'over the room', 'library', None, None, None,
                                'theatre_of_stuff', 'the_cave_system1', None, None, None, None,)
the_cave_system = Room('The Home of The Defender', 'there are several piles of odds and ends, and there appears to be'
                                                   ' an unused BOOMCORN LAUNCHER in the back of the room.', None,
                       'spell_practitioners_room', 'cavern1', None, None, None, None, None, None,
                       ['BoomcornLauncher', ])
cavern1 = Room('The_Fourbidden_Tombs_Entrance', 'skeletons and bones litter the corridor', 'Tomb_of_Fyre', None, None,
               'Tomb_of_Watur', None, 'the_cave_system', 'Tomb_of_Urth', 'Tomb_of_Aer', None, None,)
Tomb_of_Fyre = Room('Tomb_of_Fyre', 'A room with pits of lava in the floor, and columns of fire making a path.  '
                                    'There are THE GAUNTLETS OF FIRE at the end of the path,', None, None, None,
                    'cavern1', None, None, None, None, None, None,)
Tomb_of_Watur = Room('Tomb_of_Watur', 'A room with deep pools of water, and a damp mist parting to reveal a path to '
                                      'THE AQUARION HELM', None, None, None, 'cavern1', None, None, None, None,
                     None, None,)
Tomb_of_Urth = Room('Tomb_of_Urth', 'An earthy, musky room with rough spires of rock lining a path to '
                                    'THE ROCKSHARD', None, None, None, 'cavern1', None, None, None, None, None, None,)
Tomb_of_Aer = Room('Tomb_of_Aer', '___', None, None, None, 'cavern1', None, None, None, None, None, None,)
theatre_of_stuff = Room('theatre_of_stuff', 'a gladiator pit, filled with bones of the dead', None,
                        'spell_practitioners_room', None, 'mess_hall', None, None, "Double_you_building", None, None,
                        None,)
mess_hall = Room('cafeteria_land', 'a gym-like room filled with rotting food.', 'theatre_of_stuff', None, None, None,
                 None, None, None, None, None, None,)
Double_you_building = Room('Double_you_building', 'A magic testing area', 'clone_room', None, None, None, None, None,
                           'the_button_room', 'theatre_of_stuff', None, None,)
clone_room = Room('clone room', 'A cell-replication chamber', None, None, None, 'Double_you_building', None, None,
                  None, None, None, None)
the_button_room = Room('Button Room', 'A room with a pointless button', None, None, None, None, None, None, None,
                       'Double_you_building', None, None,)
frontgate3 = Room('Frontgate3', 'You are standing in front of an engraved golden gate,which appears to be the entrance'
                                ' to a castle, which could also be the mysterious yet famed, ACADEMY.', None, None,
                  None, 'parklot3', None, None, None, 'frontgate2', None, None,)
parklot3 = Room('Abandoned Lot 3', 'There are about 16 trees in the apparent orchard, and the grass is way overgrown. '
                'There are paths to the north, south, and west', 'frontgate3', None, None, 'abandoned_classroom1',
                None, None, None, 'parklot2', None, None,)
abandoned_classroom1 = Room('class_101', 'class lOl looks empty, to the naked eye...', 'parklot3', None, None,
                            'abandoned_classroom2', None, None, 'abandoned_classroom3', None, None, None,)
abandoned_classroom2 = Room('class_102', 'class lO2 looks empty, to the naked eye...', 'abandoned_classroom1', None,
                            None, None, None, None, 'abandoned_classroom4', None, None, None,)
abandoned_classroom3 = Room('class_103', 'class lO3 looks empty, to the naked eye...', None, None, None,
                            'abandoned_classroom4', None, None, 'abandoned_classroom5', 'abandoned_classroom1', None,
                            None,)
abandoned_classroom4 = Room('class 104', 'class lO4 looks empty, to the naked eye...', 'abandoned_classroom3', None,
                            None, None, None, None, 'abandoned_classroom6', 'abandoned_classroom2', None, None,)
abandoned_classroom5 = Room('class_105', 'class lO5 looks empty, to the naked eye...', None, None, None,
                            'abandoned_classroom4', None, None, 'abandoned_classroom5', 'abandoned_classroom1', None,
                            None,)
abandoned_classroom6 = Room('class_106', 'there is a pedestal with a _______', 'abandoned_classroom5', None, None, None,
                            None, None, None, 'abandoned_classroom4', None, None,)


current_node = bland_room
directions = ['north', 'northwest', 'west', 'southwest', 'south', 'southeast', 'east', 'northeast']
short_directions = ['n', 'nw', 'w', 'sw', 's', 'se', 'e', 'ne']


while True:
    # Prints the current node
    print(current_node.name)
    print(current_node.description)
    print(current_node.objects)
    print("INSTRUCTIONS"
          "")

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

    # if 'steal' in command:
    #     if current_node.item is not None:
    #         HERO.steal(current_node.item)
    #         current_node.item = None
    #         inventory.append(current_node.item)
    #     else:
    #         print("There's nothing in the room.")

    elif command[:7] == 'pick up':
        item = command[8:]
    else:
        print('Command not recognized')
