from constants import *
from levels import *
from wall import *
from interactable import *
from player import *
import pygame

pygame.init()
clock = pygame.time.Clock()
SCREEN_HEIGHT, SCREEN_WIDTH = SCREEN_DIMENSIONS
BACKGROUND_HEIGHT, BACKGROUND_WIDTH = BACKGROUND_DIMENSIONS
SURFACE = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
pygame.display.set_caption(GAME_NAME)

def main():
    running = True
    gameBackground = pygame.transform.scale(pygame.image.load("./Assets/Images/game_background.jpg"), (BACKGROUND_HEIGHT, BACKGROUND_WIDTH))
    currLevel = LEVEL_ONE
    
    # Sprite collection
    playerAnimationSprites = pygame.sprite.Group()
    wallCollectionSprites = pygame.sprite.Group()
    interactableCollectionSprites = pygame.sprite.Group()
    
    player = Player(SURFACE, COLOR_RED)
    playerAnimationSprites.add(player)
    parseGrid(currLevel, player, interactableCollectionSprites)
    for wall in walls:
        wallCollectionSprites.add(wall)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SURFACE.blit(gameBackground, (0, 0))
        # player.drawPlayerHitbox()
        player.handlePlayerKeys()
        
        drawWalls(player)
        interactableCollectionSprites.draw(SURFACE)
        player.collided = False
        
        playerAnimationSprites.draw(SURFACE)
        playerAnimationSprites.update()
        
        pygame.display.flip()
        clock.tick(GAME_TICK)
    
    pygame.quit()

# Helpers
def parseGrid(level, player, interactableCollection):
    for i in range(len(level)):
        for j in range(len(level[0])):
            char = level[j][i]
            coord_x = GRID_START[0] + (BLOCK_LENGTH * i)
            coord_y = GRID_START[0] + (BLOCK_LENGTH * j)
            
            if char == CHAR_WALL:
                wall = Wall(coord_x, coord_y)
                walls.append(wall)
            elif char == CHAR_PLAYER:
                if player.unset:
                    player.rect.x = coord_x
                    player.rect.y = coord_y
                    player.unset = False
            elif char != CHAR_EMPTY:
                interactableCollection.add(Interactable(coord_x, coord_y, char))
def drawWalls(player):
    for wall in walls:
        if player.collided == UP:
            wall.rect.y -= RUMBLE_DIST
            wall.draw(SURFACE)
            wall.rect.y += RUMBLE_DIST
        elif player.collided == DOWN:
            wall.rect.y += RUMBLE_DIST
            wall.draw(SURFACE)
            wall.rect.y -= RUMBLE_DIST
        elif player.collided == RIGHT:
            wall.rect.x += RUMBLE_DIST
            wall.draw(SURFACE)
            wall.rect.x -= RUMBLE_DIST
        elif player.collided == LEFT:
            wall.rect.x -= RUMBLE_DIST
            wall.draw(SURFACE)
            wall.rect.x += RUMBLE_DIST
        else:
            wall.draw(SURFACE)        
# Start game
main()
    
    
    