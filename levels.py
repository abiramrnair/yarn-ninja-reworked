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
        },
        {
            'name':"LEVEL 4",
            'available_moves': 13,
            'surface_grid': [
             ["-","-","-","-","-","-","-","-","-","-"],
             ["-","*","P","-","-","PP","*","*","-","-"],
             ["-","*","-","-","-","*","-","*","*","-"],
             ["-","*","-","-","-","*","*","*","-","-"],
             ["-","*","-","T","*","*","*","*","*","-"],
             ["-","*","*","-","-","*","*","*","*","-"],
             ["-","-","*","-","-","-","G","-","PP","-"],
             ["-","*","*","*","*","*","*","*","-","-"],
             ["-","*","*","-","-","-","*","*","PBRL","-"],
             ["-","-","-","-","-","-","-","-","-","-"],
            ],
            'obstacle_grid': [('PI', (6, 6))],
            'interactive_coords': {
                (8, 8): {'impact': (6, 6), 'action': 'destroy'}, # destroy the gate at 6,6
                (5,1): {'impact': (4, 4), 'action': 'teleport'},
                (8,6): {'impact': (1, 5), 'action': 'teleport'},
                (3, 4): {'impact': None, 'action': 'win'}
            }
        },{
            'name':"LEVEL 5",
            'available_moves': 13,
            'surface_grid': [
             ["-","-","-","-","-","-","-","-","-","-"],
             ["-","-","*","RBRL","-","-","-","T","*","-"],
             ["-","*","*","*","*","SLH","-","*","*","-"],
             ["-","-","*","*","-","-","-","*","-","-"],
             ["-","*","*","*","*","*","*","*","SLH","-"],
             ["-","-","*","-","-","-","*","*","*","-"],
             ["-","-","G","-","-","-","-","G","-","-"],
             ["-","*","*","*","*","*","*","*","-","-"],
             ["-","P","*","-","-","-","*","*","PBRL","-"],
             ["-","-","-","-","-","-","-","-","-","-"],
            ],
            'obstacle_grid': [('PI', (6, 2))],
            'interactive_coords': {
                (8, 8): {'impact': (2, 6), 'action': 'destroy'}, # destroy the gate at 6,6
                (3,1): {'impact': (7, 6), 'action': 'destroy'},
                # (8,6): {'impact': (1, 5), 'action': 'teleport'},
                (3, 4): {'impact': None, 'action': 'win'}
            }
        }
]
