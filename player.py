import pygame
from camera import Camera

# test comment

class Player(pygame.sprite.Sprite):
    def __init__(self, surface, cam:Camera, image_path, pos) -> None:
        # Initialise super class and load image
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.G = 9.8
        self.pos = pygame.Vector2(pos)
        self.speed = 300
        self.surface = surface
        self.cam = cam

    def set_pos(self, x: float, y: float) -> None:
        # x_b,y_b = pygame.display.get_window_size()
        # if x <= 0:
        #     x = 0
        # if x >= x_b:
        #     x = x_b
        # if y <= 0:
        #     y = 0
        # if y>= y_b:
        #     y = y_b   
        self.pos = pygame.Vector2(x,y)
        self.cam.set_pos(self.pos)

    def draw(self) -> None:
        rect = self.image.get_rect(center=self.pos)
        self.cam.draw(self.image, rect)
    
    def gravity(self,x: float,y: float,terrian: bool) -> None:
        if terrian is True:
            pass
        else:
            pass