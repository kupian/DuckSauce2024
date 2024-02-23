import pygame

class Player:
    def __init__(self, x,y):
        self.pos = pygame.Vector2(x,y)
        self.speed = 300
        self.radius = 40

    def set_pos(self, x, y):
        self.pos = pygame.Vector2(x,y)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.pos, self.radius)