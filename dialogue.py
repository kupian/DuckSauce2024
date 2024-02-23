import pygame

class DialogueBox:
    def __init__(self, surface, colour=(255,255,255)):
        WIN_HEIGHT, WIN_WIDTH = pygame.display.get_window_size()
        rect = pygame.Rect((WIN_WIDTH/2, WIN_HEIGHT/2, 200, 100))
        self.surface = surface
        self.colour = colour
        self.rect = pygame.Rect(rect)

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)
