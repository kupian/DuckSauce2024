import pygame
from player import Player
from dialogue import DialogueBox
import spriteSheet
import numpy as np
from image_audio import *
from PIL import Image  
import PIL

## no thanks to alex we have arrived at the game jam
## going to lose :)

CAMERA_SIZE = (460,256)
LEVEL_SIZE = (2560,1440)

pygame.init()
screen = pygame.display.set_mode(CAMERA_SIZE)

clock = pygame.time.Clock()
running = True

dt = 0
timer = 0
x,y = pygame.display.get_window_size()
x /=2
y/=2
timing = False

bg=Player(screen,"art/test_bg.png",(x,y))
player = Player(screen,"art/static_duck.png", (x,y))
while running:
    if timing:
        timer += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg.draw()
    player.draw()
    
    keys = pygame.key.get_pressed()
    x,y = player.pos
    if keys[pygame.K_w]:
        y -= 1000 * dt
    if keys[pygame.K_s]:
        y += 1000 * dt
    if keys[pygame.K_a]:
        x -= 1000 * dt
    if keys[pygame.K_d]:
        x += 1000 * dt
    player.set_pos(x,y)


    if keys[pygame.K_k]:
        timer = 0
        timing = True
        ss = load_image_colour("art/duckSwing.png")
        images=[]
        xPos=0
        xCounter=0
        yCounter=0
        yPos=0
        while timer <= (1/24) * 21:
            if xCounter == 4:
                xPos=0
                xCounter=0
            if yCounter == 4:
                yPos=0
                yCounter=0
            image = ss[xPos:xPos+32, yPos:yPos+32, :]
            image = ("art/duckSwingFrame.png")
            yCounter+=1
            xCounter+=1
            yPos+=32
            xPos+=32

    

            player = Player(screen,"art/duckSwingFrame.png", (x,y))
        

        n = 0

        
    pygame.display.flip()

    dt = clock.tick(60) / 1000


