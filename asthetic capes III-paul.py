world_map = {
    'FRONTGATE1': {
        'NAME': 'The first front gate',
        'DESCRIPTION': 'You are in front of a rusted iron gate which appears to be the entrance to a castle, '
                       'which could also be the mysterious yet famed, ACADEMY.',
        'PATHS': {
            'WEST': 'FRONTGATE2',
            'SOUTH': 'PARKINGLOT1',
        }
    },
    'FRONTGATE2': {
        'NAME': 'The second front gate.',
        'DESCRIPTION': 'You are standing in front of a slightly burnished silver gate which appears to be the entrance'
                       'to a castle, which could also be the mysterious yet famed, ACADEMY.  '
                       'There is a backpack next to you, but you cannot pick it up(Thanks Mr. Wiebe.).',
        'PATHS': {
            'EAST': 'FRONTGATE1',
            'WEST': 'FRONTGATE3',
            'SOUTH': 'PARKINGLOT2',
        }
    },
    'FRONTGATE3': {
        'NAME': 'The third front gate',
        'DESCRIPTION': 'You are standing in front of an engraved golden gate,which appears to be the entrance'
                       ' to a castle, which could also be the mysterious yet famed, ACADEMY.',
        'PATHS': {
            'WEST': 'FRONTGATE2',
            'SOUTH': 'PARKINGLOT3',
        }
    },
    'PARKINGLOT1': {
        'NAME': 'Parking lot A',
        'DESCRIPTION': 'There are several rusted metal objects around you.  '
                       'One of the objects doors is opened with'
                       'a strange pale-green light coming through the windshield, that disappears as you walk forward',
        'PATHS': {
            'NORTH': 'FRONTGATE1',
            'EAST': 'PARKINGLOT2',
            'SOUTH': 'HALL1'
        }
    },
    'PARKINGLOT2': {
        'NAME': 'Parking lot B',
        'DESCRIPTION': 'the ground is dry and cracked, yet the sky looks dark and stormy. '
                       'There are paths to the north, east, west, and south.',
        'PATHS': {
            'NORTH': 'FRONTGATE2',
            'EAST': 'PARKINGLOT3',
            'WEST': 'PARKINGLOT1',
            'SOUTH': 'LIBRARY',
        }
    },
    'PARKINGLOT3': {
        'NAME': 'Parking lot C',
        'DESCRIPTION': 'There are about 16 trees in the apparent orchard, and the grass is way overgrown. '
                       'There are paths to the north, south, and west',
        'PATHS': {
            'NORTH': 'FRONTGATE3',
            'WEST': 'PARKINGLOT2',
            'SOUTH': 'ABANDONDEDCLASSROOM1',
        }
    },
    'HALL1': {
        'NAME': 'Hallway',
        'DESCRIPTION': 'A hallway that has a passageway to the east and west. It appears to continue further south.',
        'PATHS': {
            'NORTH': 'PARKINGLOT1',
            'SOUTH': 'HALL2',
            'WEST': 'GYM',
            'EAST': 'CORRIDOR1',
        }
    },
    'LIBRARY': {
        'NAME': 'Spellbook research facility.',
        'DESCRIPTION': 'There are several books lying strewn about the floor. '
                       'There is a passage way to the south and to the north',
        'PATHS': {
            'SOUTH': 'COMPUTERLAB1',
            'NORTH': 'PARKINGLOT2',
        }
    },
    'ABANDONDEDCLASSROOM': {
        'NAME': 'Co put r  ab',
        'DESCRIPTION': 'Some of the letters on the door have somewhat rubbed off. There is a door to the south, '
                       'and the door you just came through leads to the north. '
                       'When you look closer around the room, however, you find another door to the east',
        'PATHS': {
            'EAST': 'WARROOM1',
            'NORTH': 'PARKINGLOT3',
            'SOUTH': 'WARROOM6'
        }
    },
    'WARROOM1': {
        'NAME': 'Battle strategy',
        'DESCRIPTION': 'there is a',
        'PATHS': {

        }
    }
}

current_node = world_map['FRONTGATE1']
directions = ['NORTH', 'NORTHWEST', 'WEST', 'SOUTHWEST', 'SOUTH', 'SOUTHEAST', 'EAST', 'NORTHEAST']
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('Your pants will fall off if you go this way!')
    else:
        print('Command not recognized')
