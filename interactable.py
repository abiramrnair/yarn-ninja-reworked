import pygame
from constants import *

# T = target, O = obstacle, G = gate, S = portal start, E = portal end
# D = danger obstacle type 1, R = danger obstacle type 2

interactables = {
    'T': pygame.transform.scale(pygame.image.load("Assets/Images/target_block.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'G': pygame.transform.scale(pygame.image.load("Assets/Images/gate_block.png"), (BLOCK_LENGTH, BLOCK_LENGTH))
}

class Interactable(pygame.sprite.Sprite):
    def __init__(self, x, y, object):
        super().__init__()
        self.image = interactables[object]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def draw(self, surface):
        surface.blit(self.image, self.rect)