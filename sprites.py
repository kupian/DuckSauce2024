import pygame
from camera import Camera
import numpy as np
from dialogue import TextBox, Quest
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
        '''
        Changes image used to display sprite.
        TODO: Incorporate collision changes
        '''
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
        except FileNotFoundError as e:
            self.collision_mask = pygame.mask.from_surface(self.image.convert_alpha())
            print(f"{self.image_path} has no collision mask! Generating one from alpha values")  

    def set_pos(self, pos:pygame.Vector2) -> None:
        # x_b,y_b = pygame.display.get_window_size()
        # if x <= 0:
        #     x = 0
        # if x >= x_b:
        #     x = x_b
        # if y <= 0:
        #     y = 0
        # if y>= y_b:
        #     y = y_b   
        self.pos = pos

    def draw(self) -> None:
        '''
        Calls camera draw method
        '''
        self.cam.draw(self.image, self.pos)

class Player(Sprite):
    '''
    Player class that inherits from Sprite
    '''
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str) -> None:
        super().__init__(surface, cam, pos,image_path)
        self.G = 3
        # h velocity will be set to hspeed when keys pressed
        self.speed = (5, -3)
        # v velocity is constantly updated with gravity
        self.velocity = [0,0]

    def move(self) -> None:
        '''
        Sets position of player and updates camera position
        '''
        # TODO: Improve collision (this shit buggy as fuck!) and check for collision with all objects
        new_pos = self.pos + self.velocity
        overlap = self.collision_mask.overlap_area(pygame.mask.from_surface(pygame.image.load("art/bgtest2_mask.png")), (-new_pos.x, -new_pos.y))
        if overlap >= 0:
            self.pos = new_pos
            self.cam.set_pos(self.pos)

    def jump(self, direction=1):
        self.velocity[1] = self.speed[1] * direction

    def set_speed(self, direction:int):
        '''
        Takes 0, +1 or -1 to represent right and left movement respectively.
        Actual speed is taken from object properties.
        '''
        self.velocity[0] = self.speed[0]*direction
        if direction == 1:
            self.set_frame("art/staticDuckRight.png")
        else:
            self.set_frame("art/static_duck.png")

    def apply_gravity(self, velocity:tuple, dt) -> list:
        '''
        Takes a velocity vector and applies gravity with respect to time
        '''
        return [velocity[0], velocity[1] + self.G*dt]
    
    def update(self, dt):
        self.velocity = self.apply_gravity(self.velocity, dt)
        if self.velocity[1] > 0:
            self.set_frame("art/flyDown.png")
        elif self.velocity[1] < 0:
            self.set_frame("art/fly.png")
        self.move()

class NPC(Sprite):
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str):
        super().__init__(surface, cam, pos, image_path)

    def set_quest(self, quest_file:str):
        self.quest = Quest(quest_file)

    def talk(self) -> list:
        return self.quest.show_current_dialogue(self.surface, self.cam)

class Enemy(Sprite):
    def __init__(self, surface:pygame.Surface, cam:Camera, pos:tuple, image_path: str, player:Player):
        super().__init__(surface, cam, pos, image_path)
        self.velocity = 50
        self.player = player
        self.health = 100

    def move(self, dt) -> pygame.Vector2:
        self.set_pos(self.pos.move_towards(self.player.pos, self.velocity*dt))
    
    def die(self):
        print("AM DED")

    def hit(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.die()

    def draw(self) -> None:
        '''
        Calls camera draw method
        '''
        bar_width = 25*(self.health/100)
        bar_height = 5
        self.cam.draw(self.image, self.pos)
        self.cam.draw(pos=(self.pos[0], self.pos[1]-bar_height*1.5), size=(bar_width,bar_height), colour=(255,0,0))