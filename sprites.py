import pygame
from camera import Camera
import numpy as np

class Sprite:
    '''
    Super class for all ingame sprites 
    '''
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path:str) -> None:
        self.surface = surface
        self.cam = cam
        self.pos = pygame.Vector2(pos)
        self.set_frame(image_path)
        self.setup_collision()

    def set_frame(self, image_path:str) -> None:
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)

    def setup_collision(self) -> None:
        '''
        Creates a collision mask from a mask image. Prints an error if no mask is provided.
        '''
        try:
            mask_path = f"{self.image_path.split('.')[0]}_mask.{self.image_path.split('.')[1]}"
            mask_surf = pygame.image.load(mask_path)
            self.collision_mask = pygame.mask.from_surface(mask_surf)
            self.image = self.collision_mask.to_surface()
        except FileNotFoundError as e:
            print(f"{self.image_path} has no collision mask! If you need collision, make sure a second image is provided with the ending _mask.png")   

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
        Calls camera draw method
        '''
        self.cam.draw(self.image, self.pos)

class Player(Sprite):
    '''
    Player class that inherits from Sprite
    '''
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str, velocity:tuple) -> None:
        super().__init__(surface, cam, pos,image_path)
        self.G = -0.2
        self.xspeed = 100
        self.yspeed = 5
        self.velocity = pygame.Vector2(velocity)

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
        new_pos = pygame.Vector2(x,y)
        overlap = self.collision_mask.overlap_area(pygame.mask.from_surface(pygame.image.load("art/bgtest2_mask.png")), (-new_pos.x, -new_pos.y))
        print(f"Trying to set player pos to {new_pos}, overlap is {overlap}")
        if overlap == 0:
            self.pos = new_pos
            self.cam.set_pos(self.pos)
    
    def getVelocity(self,direction=None):
            if direction=='y':
                return self.velocity[1]
            elif direction=='x':
                return self.velocity[0]
            return self.velocity

    def setVelocity(self,newVelocity):
            self.velocity = newVelocity
    
    def gravity(self,x: float,y: float,terrian: bool) -> None:
        if terrian is True:
            pass
        else:
            pass

class NPC(Player):
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str):
        super().__init__(surface, cam, pos, image_path)