import pygame

WIN_HEIGHT, WIN_WIDTH = pygame.display.get_window_size()

class DialogueBox:
    def __init__(self, surface, colour=(255,255,255), rect=(0,0,100,100)):
        self.surface = surface
        self.colour = colour
        self.rect = pygame.Rect(rect)

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)
