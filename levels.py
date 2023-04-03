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
             ["-","*","-","T","-","*","-","-","*","-"],
             ["-","*","-","*","-","*","-","-","*","-"],
             ["-","*","-","*","-","*","*","PBRL","*","-"],
             ["-","*","-","GP","-","-","-","-","*","-"],
             ["-","*","-","-","-","-","-","-","*","-"],
             ["-","P","*","*","*","*","*","*","*","-"],
             ["-","-","-","-","-","-","-","-","-","-"],
            ],
            'obstacle_grid': [('PI', (1, 4))],
            'interactive_coords': {
                (7, 5): {'impact': (4, 1), 'action': 'destroy'},
                (1, 1): {'impact': (3, 5), 'action': 'teleport'},
                (3, 6): {'impact': (2, 1), 'action': 'teleport'},
                (3, 3): {'impact': None, 'action': 'win'}
              }
        }
]
