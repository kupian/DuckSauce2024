import pygame
import numpy as np

class Camera:
    def __init__(self, surface, cam_size: tuple, level_size: tuple):
        self.pos = np.array((0,0))
        self.level_size = np.array(level_size)
        self.cam_size = np.array(cam_size)

    def set_pos(self, pos):
        pos = np.array(pos)
        self.pos = pos-(self.cam_size/2)
    
    def local_pos(self, global_pos: tuple) -> tuple:
        '''
        Takes a global coordinate and outputs a camera space coordinate
        '''
        global_pos = np.array(global_pos)
        local_pos = (global_pos - self.pos)
        return local_pos
    
    def draw(self, target)