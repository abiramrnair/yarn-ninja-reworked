import pygame

walls = []

class Wall:
    def __init__(self, x, y):
        walls.append(self)
        self.rect = pygame.Rect(x, y, 50, 50)