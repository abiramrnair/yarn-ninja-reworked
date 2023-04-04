from constants import *
import pygame

# Load sprites
running_left_slime_sprites = []
for i in range(6):
    image = pygame.transform.scale(pygame.image.load("Assets/Running/SlimeLeftFrame" + str(i + 1) + ".png"), (50, 50))
    running_left_slime_sprites.append(image)
    
running_right_slime_sprites = []
for i in range(6):
    image = pygame.transform.scale(pygame.image.load("Assets/Running/SlimeRightFrame" + str(i + 1) + ".png"), (50, 50))
    running_right_slime_sprites.append(image)

# SLH = slime moving horizontally, SLV = slime moving vertically 
enemy_sprite_stances = {
    'SLH': [running_left_slime_sprites, running_right_slime_sprites], # when moving horizontally slime look changes
    'SLV': [running_left_slime_sprites]
}

enemy_direction = {
    'SLH': (ENEMY_MOVE_SPEED, 0),
    'SLV': (0, ENEMY_MOVE_SPEED)
}
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.current_stance = 0
        self.currentSprite = 0
        self.image = enemy_sprite_stances[type][self.current_stance][self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.walls = None
        self.autoMoving = True
        self.oppositeDir = 1
    def update(self):
        if self.autoMoving:
            self.move()
        self.currentSprite += ENEMY_ANIM_INC
        if self.currentSprite >= len(enemy_sprite_stances[self.type][self.current_stance]):
            self.currentSprite = 0
        self.image = enemy_sprite_stances[self.type][self.current_stance][int(self.currentSprite)]
    def move(self):
        dx = enemy_direction[self.type][0] * self.oppositeDir
        dy = enemy_direction[self.type][1] * self.oppositeDir
        self.rect.x += dx
        self.rect.y += dy

        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                self.oppositeDir *= -1
                if dx > 0: 
                    self.rect.right = wall.rect.left
                    self.current_stance = 0
                    self.collided = RIGHT
                if dx < 0: 
                    self.rect.left = wall.rect.right
                    self.current_stance = 1
                    self.collided = LEFT
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    self.collided = UP
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                    self.collided = DOWN