from constants import *
from levels import *
from wall import *
from interactable import *
from enemy import *
from player import *
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH = SCREEN_DIMENSIONS
        self.BACKGROUND_HEIGHT, self.BACKGROUND_WIDTH = BACKGROUND_DIMENSIONS
        self.SURFACE = pygame.display.set_mode([self.SCREEN_HEIGHT, self.SCREEN_WIDTH])
        self.walls = []
        # Sprite collection
        self.playerAnimationSprites = pygame.sprite.Group()
        self.enemyAnimationSprites = pygame.sprite.Group()
        self.wallCollectionSprites = pygame.sprite.Group()
        self.interactableCollectionSprites = pygame.sprite.Group()
        pygame.display.set_caption(GAME_NAME)
    def main(self, level):
        running = True
        gameBackground = pygame.transform.scale(pygame.image.load("./Assets/Images/background.jpg"), (self.BACKGROUND_HEIGHT, self.BACKGROUND_WIDTH))
        currLevel = GAME_LEVELS[level]
        resetLevel = False
        showLevelInfo = True

        # Player setup
        player = Player(self.SURFACE, COLOR_RED)
        player.available_moves = currLevel['available_moves']
        player.interactableCollection = self.interactableCollectionSprites
        player.interactableCoords = currLevel['interactive_coords']
        self.playerAnimationSprites.add(player)

        # font
        pygame.font.init()
        font = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 20)
        
        # Grid setup
        self.parseGrid(currLevel, player, self.interactableCollectionSprites)
        for wall in self.walls:
            self.wallCollectionSprites.add(wall)
        player.walls = self.walls
        for sprite in self.enemyAnimationSprites:
            sprite.walls = self.walls
        
        # Game loop
        while running:
            level_label = font.render(str(currLevel["name"]), True, COLOR_WHITE)
            moves_label = font.render('Moves  ' + str(player.available_moves), True, COLOR_WHITE)
            colon_label = pygame.font.SysFont('Arial', 28,bold=True).render(' :',True, COLOR_WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    # return "end"

            self.SURFACE.blit(gameBackground, (0, 0))
            # player.drawPlayerHitbox()
            player.handlePlayerKeys()

            self.drawWalls(player)
            self.enemyAnimationSprites.draw(self.SURFACE)
            self.enemyAnimationSprites.update()
            self.interactableCollectionSprites.draw(self.SURFACE)
            self.interactableCollectionSprites.update()
            player.collided = False

            self.playerAnimationSprites.draw(self.SURFACE)
            self.playerAnimationSprites.update()

            # check if the timeout duration has elapsed and reset the level
            if resetLevel:
                pygame.time.delay(2500)
                self.cleanUpRender()
                self.main(0)
            if player.win:
                level_completed_label = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 30).render(
                   str(currLevel["name"]) + " Completed", True, COLOR_WHITE)
                self.SURFACE.blit(level_completed_label, (self.SCREEN_WIDTH / 2 - 240, 30))
                pygame.display.flip()
                pygame.time.delay(2500)
                self.cleanUpRender()
                if level + 1 < len(GAME_LEVELS):
                    self.main(level + 1)
                else:
                    import Main
                    Main.home()
            if player.available_moves <= 0:
                level_label = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 40).render("Game Over", True,
                                                                                             COLOR_WHITE)
                self.SURFACE.blit(level_label, (self.SCREEN_WIDTH / 2 - 170, 20))
                resetLevel = True
            else:
                self.SURFACE.blit(level_label, (10, 10))
                self.SURFACE.blit(moves_label, (self.SCREEN_WIDTH - 165, 10))
                self.SURFACE.blit(colon_label, (self.SCREEN_WIDTH - 60, 4))

            pygame.display.update()
            self.clock.tick(GAME_TICK)

        pygame.quit()

    # Helpers
    def parseGrid(self, level, player, interactableCollection):
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
                    self.walls.append(wall)
                elif char == CHAR_PLAYER:
                    if player.unset:
                        player.rect.x = coord_x
                        player.rect.y = coord_y
                        player.unset = False
                elif char == CHAR_SLIME_HORIZONTAL or char == CHAR_SLIME_VERTICAL:
                    self.enemyAnimationSprites.add(Enemy(coord_x, coord_y, char))
                elif char != CHAR_EMPTY:
                    interactableCollection.add(Interactable(coord_x, coord_y, char))
    def drawWalls(self, player):
        for wall in self.walls:
            if player.collided == UP:
                wall.rect.y -= RUMBLE_DIST
                wall.draw(self.SURFACE)
                wall.rect.y += RUMBLE_DIST
            elif player.collided == DOWN:
                wall.rect.y += RUMBLE_DIST
                wall.draw(self.SURFACE)
                wall.rect.y -= RUMBLE_DIST
            elif player.collided == RIGHT:
                wall.rect.x += RUMBLE_DIST
                wall.draw(self.SURFACE)
                wall.rect.x -= RUMBLE_DIST
            elif player.collided == LEFT:
                wall.rect.x -= RUMBLE_DIST
                wall.draw(self.SURFACE)
                wall.rect.x += RUMBLE_DIST
            else:
                wall.draw(self.SURFACE)
    def cleanUpRender(self):
        self.playerAnimationSprites.empty()
        self.wallCollectionSprites.empty()
        self.interactableCollectionSprites.empty()
        self.walls = []
        self.enemyAnimationSprites.empty()