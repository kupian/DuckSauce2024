import pygame
import numpy as np

class Camera:
    def __init__(self, cam_size: tuple, level_size: tuple):
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
        print(f"global pos {global_pos} self pos {self.pos}")
        print(f"{global_pos - self.pos}")
        local_pos = ((global_pos - self.pos)/self.level_size)*self.cam_size
        print(f"Local pos {local_pos}")
        return local_pos
    
    def local_size(self, global_size: tuple) -> tuple:
        global_size = np.array(global_size)
        local_size = (global_size/self.level_size)*self.cam_size
        return local_size
    