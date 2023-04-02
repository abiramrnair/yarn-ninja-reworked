# Pygame
GAME_TICK = 60
GAME_NAME = "Yarn Ninja"
SCREEN_DIMENSIONS = (700, 700)
BACKGROUND_DIMENSIONS = (800, 800)

# Colors
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)

# Environment
GRID_START = (100, 100)
BLOCK_LENGTH = 50
CHAR_WALL = "-"
CHAR_PLAYER = "P"
CHAR_EMPTY = "*"
RUMBLE_DIST = 3
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"

# Player
PLAYER_MOVESPEED = 8
PLAYER_ANIM_INC = 0.30
PLAYER_HITBOX_X = 50
PLAYER_HITBOX_Y = 50
PLAYER_DESTROY = "destroy"
PLAYER_TELEPORT = "teleport"
PLAYER_WIN = "win"

# Coords functions
def getTranslatedCoords(startingCoords, coord):
    return startingCoords[0] + (BLOCK_LENGTH * coord[0]), startingCoords[0] + (BLOCK_LENGTH * coord[1])
def getOriginalCoords(startingCoords, translatedCoords):
    return (translatedCoords[0] - startingCoords[0]) // BLOCK_LENGTH, (translatedCoords[1] - startingCoords[0]) // BLOCK_LENGTH