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
                           'It appears to continue further south.', 'parklot1', None, None, 'hallway1', None, None,
                "room 23", "gym")

current_node = bland_room
directions = ['north', 'northwest', 'west', 'southwest', 'south', 'southeast', 'east', 'northeast']
short_directions = ['n', 'nw', 'w', 'sw', 's', 'se', 'e', 'ne']


while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('Your pants will fall off if you go this way!')
    else:
        print('Command not recognized')
