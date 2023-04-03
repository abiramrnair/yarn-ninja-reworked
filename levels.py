GAME_LEVELS = [
        {
            'name': "LEVEL 1",
            'available_moves': 8,
            'surface_grid': [
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "T", "*", "*", "-", "*", "*", "*", "*", "-"],
                ["-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
                ["-", "P", "-", "*", "-", "*", "-", "-", "*", "-"],
                ["-", "*", "-", "*", "-", "*", "-", "-", "*", "-"],
                ["-", "*", "-", "*", "-", "*", "-", "-", "*", "-"],
                ["-", "*", "-", "*", "*", "*", "-", "-", "*", "-"],
                ["-", "*", "-", "-", "-", "-", "-", "-", "*", "-"],
                ["-", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ],
            'obstacle_grid': [],
            'interactive_coords': {
              (1, 1): {'impact': None, 'action': 'win'}
            }
        },
        {
             'name': "LEVEL 2",
             'available_moves': 8,
             'surface_grid': [
             ["-","-","-","-","-","-","-","-","-","-"],
             ["-","GP","*","*","G","*","*","*","*","-"],
             ["-","-","-","-","-","*","-","-","*","-"],
             ["-","-","-","T","-","*","-","-","*","-"],
             ["-","P","-","*","-","*","-","-","*","-"],
             ["-","*","-","*","-","*","*","PBRL","*","-"],
             ["-","*","-","GP","-","-","-","-","*","-"],
             ["-","*","-","-","-","-","-","-","*","-"],
             ["-","*","*","*","*","*","*","*","*","-"],
             ["-","-","-","-","-","-","-","-","-","-"],
            ],
            'obstacle_grid': [('PI', (1, 4))],
            'interactive_coords': {
                (7, 5): {'impact': (4, 1), 'action': 'destroy'},
                (1, 1): {'impact': (3, 5), 'action': 'teleport'},
                (3, 6): {'impact': (2, 1), 'action': 'teleport'},
                (3, 3): {'impact': None, 'action': 'win'}
              }
        },
        {
        'name': "LEVEL 3",
        'available_moves': 10,
        'surface_grid': [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "T", "*", "*", "*", "*", "-", "-", "PP", "-"],
            ["-", "-", "-", "-", "-", "*", "-", "-", "*", "-"],
            ["-", "*", "*", "*", "*", "*", "-", "-", "*", "-"],
            ["-", "*", "-", "-", "-", "-", "-", "-", "*", "-"],
            ["-", "*", "-", "RBRR", "*", "*", "*", "*", "*", "-"],
            ["-", "*", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "G", "*", "*", "*", "*", "*", "*", "PP", "-"],
            ["-", "-", "P", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ],

        'obstacle_grid': [('RI', (7, 1))],

        'interactive_coords':
            {

                (8, 7): {'impact': (8, 2), 'action': 'teleport'},
                (8, 1): {'impact': (7, 7), 'action': 'teleport'},
                (3, 5): {'impact': (1, 7), 'action': 'destroy'},
                (1, 1): {'impact': None, 'action': 'win'}

            }
        }
]
