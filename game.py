from constants import *
from levels import *
from wall import *
from player import *
import pygame   

pygame.init()
clock = pygame.time.Clock()
SCREEN_HEIGHT, SCREEN_WIDTH = SCREEN_DIMENSIONS
SURFACE = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
pygame.display.set_caption(GAME_NAME)

def main():
    running = True
    currLevel = LEVEL_ONE
    player = Player(SURFACE, COLOR_RED)
    parseGrid(currLevel, player)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        SURFACE.fill(COLOR_WHITE)
        player.drawPlayer()
        player.handlePlayerKeys()
        drawWalls()
        
        pygame.display.flip()
        clock.tick(GAME_TICK)
    
    pygame.quit()

# Helpers
def parseGrid(level, player):
    for i in range(len(level)):
        for j in range(len(level[0])):
            char = level[j][i]
            coord_x = GRID_START[0] + (50 * i)
            coord_y = GRID_START[0] + (50 * j)
            
            if char == CHAR_WALL:
                wall = Wall(coord_x, coord_y)
                walls.append(wall)
            if char == CHAR_PLAYER:
                if not hasattr(player, 'rect'):
                    player.makeRect(coord_x, coord_y)

def drawWalls():
    for wall in walls:
        pygame.draw.rect(SURFACE, COLOR_BLACK, wall.rect)

# Start game
main()
    
    
    