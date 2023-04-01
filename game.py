from constants import *
from levels import *
from wall import *
from interactable import *
from player import *
import pygame
import time

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
    resetLevel = False

    # Sprite collection
    playerAnimationSprites = pygame.sprite.Group()
    wallCollectionSprites = pygame.sprite.Group()
    interactableCollectionSprites = pygame.sprite.Group()

    # Player setup
    player = Player(SURFACE, COLOR_RED)
    player.available_moves = currLevel['available_moves']
    player.interactableCollection = interactableCollectionSprites
    player.interactableCoords = currLevel['interactive_coords']
    playerAnimationSprites.add(player)

    # font
    pygame.font.init()
    font =  pygame.font.SysFont('Arial', 25, bold=True)

    # timeout
    timeout_duration = 3000
    # Grid setup
    parseGrid(currLevel, player, interactableCollectionSprites)
    for wall in walls:
        wallCollectionSprites.add(wall)

    # Game loop
    while running:
        level_label = font.render(str(currLevel["name"]), True, COLOR_BLACK)
        moves_label = font.render('Moves: ' + str(player.available_moves), True, COLOR_BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # return "end"



        SURFACE.blit(gameBackground, (0, 0))
        # player.drawPlayerHitbox()
        player.handlePlayerKeys()
        drawWalls(player)
        interactableCollectionSprites.draw(SURFACE)
        interactableCollectionSprites.update()
        player.collided = False

        playerAnimationSprites.draw(SURFACE)
        playerAnimationSprites.update()

        # check if the timeout duration has elapsed and reset the level
        if resetLevel:
            time.sleep(3)
            main()

        if player.available_moves <= 0:
            level_label = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 30).render("Game Over", True, COLOR_BLACK)
            SURFACE.blit(level_label, (SCREEN_WIDTH/2 - 115, 20))
            resetLevel = True
            start_time = pygame.time.get_ticks()

        else:
            SURFACE.blit(level_label, (10, 10))
            SURFACE.blit(moves_label, (SCREEN_WIDTH - 115, 10))

        pygame.display.flip()
        clock.tick(GAME_TICK)

    pygame.quit()

# Helpers
def parseGrid(level, player, interactableCollection):
    grid_layer_one = level['obstacle_grid']
    grid_layer_two = level['surface_grid']
    for obstacle in grid_layer_one:
            type, coord = obstacle
            coord_x, coord_y = getTranslatedCoords(GRID_START, coord)
            interactableCollection.add(Interactable(coord_y, coord_x, type))
    for i in range(len(grid_layer_two)):
        for j in range(len(grid_layer_two[0])):
            char = grid_layer_two[j][i]
            coord_x, coord_y = getTranslatedCoords(GRID_START, (i, j))

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
# # Start game
# main()
    
    
    