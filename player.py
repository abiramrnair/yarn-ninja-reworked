import pygame
from constants import *
from wall import *   

class Player:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        self.isMoving = False
    def makeRect(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_HITBOX_X, PLAYER_HITBOX_Y)
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
                if dx < 0: 
                    self.rect.left = wall.rect.right
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
    def handlePlayerKeys(self):
        key_pressed = pygame.key.get_pressed()
        
        if (key_pressed[pygame.K_LEFT] or self.isMoving == "left") and self.isMoving != "right" and self.isMoving != "up" and self.isMoving != "down":
            self.isMoving = "left"
            self.move(-10, 0)
        if (key_pressed[pygame.K_RIGHT] or self.isMoving == "right") and self.isMoving != "left" and self.isMoving != "up" and self.isMoving != "down":
            self.isMoving = "right"
            self.move(10, 0)
        if (key_pressed[pygame.K_UP] or self.isMoving == "up") and self.isMoving != "right" and self.isMoving != "left" and self.isMoving != "down":
            self.isMoving = "up"
            self.move(0, -10)
        if (key_pressed[pygame.K_DOWN] or self.isMoving == "down") and self.isMoving != "right" and self.isMoving != "up" and self.isMoving != "left":
            self.isMoving = "down"
            self.move(0, 10)
    def drawPlayer(self):
        if hasattr(self, 'rect'):
            pygame.draw.rect(self.surface, self.color, self.rect)