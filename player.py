import pygame   

class Player:
    def __init__(self, x, y, color, surface):
        self.x = x
        self.y = y
        self.color = color
        self.surface = surface
        self.hitbox_x = 50
        self.hitbox_y = 50
    def movePlayer(self):
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_LEFT]:
            self.x -= 1
        if key_pressed[pygame.K_RIGHT]:
            self.x += 1
        if key_pressed[pygame.K_UP]:
            self.y -= 1
        if key_pressed[pygame.K_DOWN]:
            self.y += 1

    def drawPlayer(self):
        if self.x and self.y:
            player = pygame.Rect(self.x, self.y, self.hitbox_x, self.hitbox_y)
            pygame.draw.rect(self.surface, self.color, player)