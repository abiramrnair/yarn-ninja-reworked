from constants import *
from levels import *
from player import *
import pygame   

pygame.init()
clock = pygame.time.Clock()

def main():
    SCREEN_HEIGHT, SCREEN_WIDTH = SCREEN_DIMENSIONS
    surface = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    pygame.display.set_caption(GAME_NAME)
    running = True
    currLevel = LEVEL_ONE
    player = Player(None, None, COLOR_RED, surface)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(COLOR_WHITE)
        player.drawPlayer()
        player.movePlayer()
        makeGrid(surface, currLevel, player)
        
        pygame.display.flip()
        clock.tick(GAME_TICK)
    
    pygame.quit()

# Helpers
def makeGrid(surface, level, player):
    for i in range(len(level)):
        for j in range(len(level[0])):
            char = level[j][i]
            coord_x = GRID_START[0] + (50 * i)
            coord_y = GRID_START[0] + (50 * j)
            object = pygame.Rect(coord_x, coord_y, 50, 50)
            
            if char == CHAR_WALL:
                pygame.draw.rect(surface, COLOR_BLACK, object)
            if char == CHAR_PLAYER:
                if not player.x and not player.y:
                    player.x = coord_x
                    player.y = coord_y

# Start game
main()
    
    
    