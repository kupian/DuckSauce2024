import pygame
import numpy as np

class Camera:
    '''
    Follows player around the map and draws visible objects
    '''
    def __init__(self, surface, cam_size: tuple, level_size: tuple):
        self.pos = np.array((0,0))
        self.cam_size = np.array(cam_size)
        self.surface = surface

    def set_pos(self, player_pos):
        '''
        Takes a player position and centres camera on player
        TODO: I don't think player is correctly centered to camera. Needs fixing.
        '''
        player_pos = np.array(player_pos)
        
        self.pos = player_pos-(self.cam_size/2)
    
    def local_pos(self, global_pos: tuple) -> tuple:
        '''
        Takes a global coordinate and outputs a camera space coordinate for drawing
        '''
        global_pos = np.array(global_pos)
        local_pos = (global_pos - self.pos)
        return local_pos
    
    def draw(self, surface = None, pos=(0,0), size=(100,100), colour = (255,255,255)):
        '''
        Takes a surface and/or rectangle and displays it on the screen
        '''
        local_pos = self.local_pos(pos)
        if surface:
            self.surface.blit(surface, local_pos)
        else:
            pygame.draw.rect(self.surface, colour, pygame.rect.Rect(local_pos, size))
