import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, surface, image_path, pos):
        self.surface = surface
        self.image = pygame.image.load(image_path)
        self.pos = pos

    def draw(self) -> None:
        self.rect = self.image.get_rect(center=self.pos)
        self.surface.blit(self.image, self.rect)