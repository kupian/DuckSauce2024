import pygame
import numpy as np

class Camera:
    '''
    Follows player around the map and draws objects according to current view
    '''
    def __init__(self, surface, cam_size: tuple, level_size: tuple):
        self.pos = np.array((0,0))
        self.cam_size = np.array(cam_size)
        self.surface = surface

    def set_pos(self, player_pos):
        '''
        Takes a player position and centres camera on player
        '''
        player_pos = np.array(player_pos)
        self.pos = player_pos-(self.cam_size/2)
    
    def local_pos(self, global_pos: tuple) -> tuple:
        '''
        Takes a global coordinate and outputs a camera space coordinate
        '''
        global_pos = np.array(global_pos)
        local_pos = (global_pos - self.pos)
        return local_pos
    
    def draw(self, surface = None, rect = None, colour = (255,255,255)):
        '''
        Takes a surface and/or rectangle and displays it on the screen
        '''
        local_x,local_y = self.local_pos((rect.x, rect.y))
        rect.x = local_x
        rect.y = local_y
        if surface:
            self.surface.blit(surface, rect)
        elif rect:
            pygame.draw.rect(self.surface, colour, rect)
