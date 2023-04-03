import pygame
from constants import *

# T = target, O = obstacle, G = gate, PP = purple portal, GP = green portal
# D = danger obstacle type 1, R = danger obstacle type 2, PB = purple button,
# RB = red button, PI = purple indicator, RI = red indicator

interactables = {
    'T': pygame.transform.scale(pygame.image.load("Assets/Images/target_block.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'G': pygame.transform.scale(pygame.image.load("Assets/Images/gate_block.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'GP': pygame.transform.scale(pygame.image.load("Assets/Images/green_portal.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'PP': pygame.transform.scale(pygame.image.load("Assets/Images/purple_portal.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'RBRL': pygame.transform.scale(pygame.image.load("Assets/Images/red_button_rotleft.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'RBRR': pygame.transform.scale(pygame.image.load("Assets/Images/red_button_rotright.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'PBRL': pygame.transform.scale(pygame.image.load("Assets/Images/purple_button_rotleft.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'PI': pygame.transform.scale(pygame.image.load("Assets/Images/purple_indicator.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
    'RI': pygame.transform.scale(pygame.image.load("Assets/Images/red_indicator.png"), (BLOCK_LENGTH, BLOCK_LENGTH)),
}

solid_bodies = ['T', 'G', 'O', 'RBRL', 'PBRL', 'RBRR', 'PBRR']
rotate_anim_types = ('GP', 'PP')

class Interactable(pygame.sprite.Sprite):
    def __init__(self, x, y, object):
        super().__init__()
        self.image = interactables[object]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.type = object
        self.angle = 0
        self.last_rotate_anim = pygame.time.get_ticks()
        self.is_solid = True if self.type in solid_bodies else False
        self.is_portal = True if self.type in rotate_anim_types else False
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if self.type in rotate_anim_types:
            self.rotateAnim()
    def rotateAnim(self):
        if pygame.time.get_ticks() - self.last_rotate_anim > 100:
            self.last_rotate_anim = pygame.time.get_ticks()
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect(center=self.rect.center)