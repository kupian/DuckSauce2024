import pygame
from camera import Camera

class Sprite:
    '''
    Super class for all ingame sprites 
    '''
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple) -> None:
        self.surface = surface
        self.cam = cam
        self.pos = pos

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

    def draw(self) -> None:
        '''
        Gets a rect according to image size and calls camera draw method
        '''
        rect = self.image.get_rect(center=self.pos)
        self.cam.draw(self.image, rect)

class Player(Sprite):
    '''
    Player class that inherits from Sprite
    '''
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str) -> None:
        super().__init__(surface, cam, pos)
        self.image = pygame.image.load(image_path)
        self.G = 9.8
        self.pos = pygame.Vector2(self.pos)
        self.speed = 300

    def set_pos(self, x: float, y: float) -> None:
        '''
        Sets position of player and updates camera position
        '''
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
    
    def gravity(self,x: float,y: float,terrian: bool) -> None:
        if terrian is True:
            pass
        else:
            pass

class NPC(Player):
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str):
        super().__init__(surface, cam, pos, image_path)