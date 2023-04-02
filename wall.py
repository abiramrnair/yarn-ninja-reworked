import pygame
from constants import *

walls = []

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        walls.append(self)
        self.image = pygame.transform.scale(pygame.image.load("Assets/Images/wall_block.png"), (BLOCK_LENGTH, BLOCK_LENGTH))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def draw(self, surface):
        surface.blit(self.image, self.rect)

