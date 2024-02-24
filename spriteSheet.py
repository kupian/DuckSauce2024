import pygame

def get_image(sheet,frame,width):
    image = pygame.Surface((width,width)).convert_alpha()
    image.blit(sheet,(0,0),((frame*width),0,width,width))
    image.set_colorkey((0,0,0))
    return image