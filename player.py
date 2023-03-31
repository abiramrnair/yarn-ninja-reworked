import pygame
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
                self.isMoving = False
                if dx > 0: 
                    self.rect.right = wall.rect.left
                    self.current_stance = 0
                    self.collided = "right"
                if dx < 0: 
                    self.rect.left = wall.rect.right
                    self.current_stance = 2
                    self.collided = "left"
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    self.current_stance = 4
                    self.collided = "up"
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                    self.current_stance = 6
                    self.collided = "down"
    def handlePlayerKeys(self):
        key_pressed = pygame.key.get_pressed()
        
        if (key_pressed[pygame.K_RIGHT] or self.isMoving == "right") and self.isMoving != "left" and self.isMoving != "up" and self.isMoving != "down":
            self.isMoving = "right"
            self.current_stance = 1
            self.move(PLAYER_MOVESPEED, 0)
        if (key_pressed[pygame.K_LEFT] or self.isMoving == "left") and self.isMoving != "right" and self.isMoving != "up" and self.isMoving != "down":
            self.isMoving = "left"
            self.current_stance = 3
            self.move(-PLAYER_MOVESPEED, 0)
        if (key_pressed[pygame.K_UP] or self.isMoving == "up") and self.isMoving != "right" and self.isMoving != "left" and self.isMoving != "down":
            self.isMoving = "up"
            self.current_stance = 5
            self.move(0, -PLAYER_MOVESPEED)
        if (key_pressed[pygame.K_DOWN] or self.isMoving == "down") and self.isMoving != "right" and self.isMoving != "up" and self.isMoving != "left":
            self.isMoving = "down"
            self.current_stance = 7
            self.move(0, PLAYER_MOVESPEED)
    def drawPlayerHitbox(self): # For testing
        pygame.draw.rect(self.surface, self.color, self.rect)