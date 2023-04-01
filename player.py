import pygame, time
from constants import *
from wall import *   

# Load sprites
idle_sprites_right = []
for i in range(1):
    image = pygame.transform.scale(pygame.image.load("Assets/Idle/IdleRightFrame" + str(i + 1) + ".png"), (50, 50))
    idle_sprites_right.append(image)
    
running_right_sprites = []
for i in range(6):
    image = pygame.transform.scale(pygame.image.load("Assets/Running/RunRightFrame" + str(i + 1) + ".png"), (50, 50))
    running_right_sprites.append(image)

idle_sprites_left = []
for i in range(1):
    image = pygame.transform.scale(pygame.image.load("Assets/Idle/IdleLeftFrame" + str(i + 1) + ".png"), (50, 50))
    idle_sprites_left.append(image)

running_left_sprites = []
for i in range(6):
    image = pygame.transform.scale(pygame.image.load("Assets/Running/RunLeftFrame" + str(i + 1) + ".png"), (50, 50))
    running_left_sprites.append(image)

idle_sprites_up = []
for i in range(1):
    image = pygame.transform.scale(pygame.image.load("Assets/Idle/IdleUpFrame" + str(i + 1) + ".png"), (50, 50))
    idle_sprites_up.append(image)

running_up_sprites = []
for i in range(6):
    image = pygame.transform.scale(pygame.image.load("Assets/Running/RunUpFrame" + str(i + 1) + ".png"), (50, 50))
    running_up_sprites.append(image)

idle_sprites_down = []
for i in range(1):
    image = pygame.transform.scale(pygame.image.load("Assets/Idle/IdleDownFrame" + str(i + 1) + ".png"), (50, 50))
    idle_sprites_down.append(image)

running_down_sprites = []
for i in range(6):
    image = pygame.transform.scale(pygame.image.load("Assets/Running/RunDownFrame" + str(i + 1) + ".png"), (50, 50))
    running_down_sprites.append(image)

# Stance by index
# 0 = idle right, 1 = running right, 2 = idle left, 3 = running left
# 4 = idle up, 5 = running up, 6 = idle down, 7 = running down
player_stances = [
                   idle_sprites_right, running_right_sprites, 
                   idle_sprites_left, running_left_sprites,
                   idle_sprites_up, running_up_sprites,
                   idle_sprites_down, running_down_sprites
                 ]

class Player(pygame.sprite.Sprite):
    def __init__(self, surface, color):
        super().__init__()
        self.unset = True
        self.surface = surface
        self.color = color
        self.isMoving = False
        self.collided = False
        self.current_stance = 0
        self.currentSprite = 0
        self.image = player_stances[self.current_stance][self.currentSprite]
        self.rect = self.image.get_rect()
        self.collision_sound = pygame.mixer.Sound('./Assets/Sounds/CollisionSound.mp3')
        self.last_collided_time = pygame.time.get_ticks()
        self.last_collision_sound_time = pygame.time.get_ticks()
        self.interactableCollection = None
        self.interactableCoords = None
    def update(self):
        self.currentSprite += PLAYER_ANIM_INC
        if self.currentSprite >= len(player_stances[self.current_stance]):
            self.currentSprite = 0
        self.image = player_stances[self.current_stance][int(self.currentSprite)]
    def move(self, dx, dy):
        if dx != 0:
            self.moveSingleAxis(dx, 0)
        if dy != 0:
            self.moveSingleAxis(0, dy)
    def moveSingleAxis(self, dx, dy):
        self.rect.x += dx 
        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.last_collided_time = pygame.time.get_ticks()
                self.playCollisionSound()
                self.isMoving = False
                if dx > 0: 
                    self.rect.right = wall.rect.left
                    self.current_stance = 0
                    self.collided = RIGHT
                if dx < 0: 
                    self.rect.left = wall.rect.right
                    self.current_stance = 2
                    self.collided = LEFT
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    self.current_stance = 4
                    self.collided = UP
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                    self.current_stance = 6
                    self.collided = DOWN
        for sprite in self.interactableCollection:
            if sprite.is_solid and self.rect.colliderect(sprite.rect):
                self.last_collided_time = pygame.time.get_ticks()
                self.playCollisionSound()
                sprite_x, sprite_y = getOriginalCoords(GRID_START, (sprite.rect.x, sprite.rect.y))
                self.performPlayerAction(sprite_x, sprite_y)
                self.isMoving = False
                if dx > 0: 
                    self.rect.right = sprite.rect.left
                    self.current_stance = 0
                    self.collided = RIGHT
                if dx < 0: 
                    self.rect.left = sprite.rect.right
                    self.current_stance = 2
                    self.collided = LEFT
                if dy < 0:
                    self.rect.top = sprite.rect.bottom
                    self.current_stance = 4
                    self.collided = UP
                if dy > 0: 
                    self.rect.bottom = sprite.rect.top
                    self.current_stance = 6
                    self.collided = DOWN
            elif self.rect.colliderect(sprite.rect):
                sprite_x, sprite_y = getOriginalCoords(GRID_START, (sprite.rect.x, sprite.rect.y))
                self.performPlayerAction(sprite_x, sprite_y) 
    def handlePlayerKeys(self):
        key_pressed = pygame.key.get_pressed()
        if (key_pressed[pygame.K_RIGHT] or self.isMoving == RIGHT) and self.isMoving != LEFT and self.isMoving != UP and self.isMoving != DOWN:
            self.isMoving = RIGHT
            self.current_stance = 1
            self.move(PLAYER_MOVESPEED, 0)
        if (key_pressed[pygame.K_LEFT] or self.isMoving == LEFT) and self.isMoving != RIGHT and self.isMoving != UP and self.isMoving != DOWN:
            self.isMoving = LEFT
            self.current_stance = 3
            self.move(-PLAYER_MOVESPEED, 0)
        if (key_pressed[pygame.K_UP] or self.isMoving == UP) and self.isMoving != RIGHT and self.isMoving != LEFT and self.isMoving != DOWN:
            self.isMoving = UP
            self.current_stance = 5
            self.move(0, -PLAYER_MOVESPEED)
        if (key_pressed[pygame.K_DOWN] or self.isMoving == DOWN) and self.isMoving != RIGHT and self.isMoving != UP and self.isMoving != LEFT:
            self.isMoving = DOWN
            self.current_stance = 7
            self.move(0, PLAYER_MOVESPEED)
    def drawPlayerHitbox(self): # For testing
        pygame.draw.rect(self.surface, self.color, self.rect)
    def playCollisionSound(self):
        if self.last_collided_time - self.last_collision_sound_time > 300:
            self.collision_sound.play()
            self.last_collision_sound_time = pygame.time.get_ticks()
    def performPlayerAction(self, sprite_x, sprite_y):
        if (sprite_x, sprite_y) in self.interactableCoords:
            obj = self.interactableCoords[(sprite_x, sprite_y)]
            impact, action = obj['impact'], obj['action']

            if action == PLAYER_DESTROY:
                for sprite in self.interactableCollection:
                    coord_x, coord_y = getOriginalCoords(GRID_START,(sprite.rect.x, sprite.rect.y))
                    if sprite.is_solid and coord_x == impact[0] and coord_y == impact[1]:
                        sprite.kill()
            elif action == PLAYER_TELEPORT:
                for sprite in self.interactableCollection:
                    if sprite.is_portal:
                        player_x, player_y = getOriginalCoords(GRID_START, (self.rect.x, self.rect.y))
                        coord_x, coord_y = getOriginalCoords(GRID_START,(sprite.rect.x, sprite.rect.y))
                        if player_x == coord_x and player_y == coord_y:
                            self.rect.x, self.rect.y = getTranslatedCoords(GRID_START, impact)
