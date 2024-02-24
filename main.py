import pygame
from dialogue import DialogueBox
import spriteSheet
from camera import Camera
from sprites import *
import numpy as np

## no thanks to alex we have arrived at the game jam
## going to lose :)


CAMERA_SIZE = (460,256)
LEVEL_SIZE = (2560,1440)

pygame.init()

screen = pygame.display.set_mode(CAMERA_SIZE)
cam = Camera(screen, CAMERA_SIZE, LEVEL_SIZE)

clock = pygame.time.Clock()
running = True

dt = 0
timer = 0
x,y = pygame.display.get_window_size()
x /=2
y/=2
v_x = 0
v_y = 1
# Used for animations WIP
timing = False

bg=Sprite(screen, cam, (x,y), "art/bgtest2.png")

player = Player(screen, cam, (x,y),"art/static_duck.png",(v_x,v_y))
while running:
    

    if timing:
        timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # Testing object
    obj = pygame.rect.Rect(20,20,100,100)
    bg.draw()
    player.draw()

    # Draw object with camera. Object should be converted to a sprite object and draw called that way
    # instead of directly on the camera
    cam.draw(rect=obj, colour=(255,0,0))
    
    keys = pygame.key.get_pressed()
    x,y = player.pos

    v_y += 0.1
    if v_y > 5:
        v_y = 5
    player.setVelocity((v_x,v_y))
    y += player.getVelocity('y')
    if keys[pygame.K_w]:
        y -= player.yspeed * dt
        v_y -= player.yspeed
        player.setVelocity((v_x,v_y))

    if keys[pygame.K_s]:
        y += player.yspeed * dt
        player.setVelocity((v_x,v_y))
    if keys[pygame.K_a]:
        player.getVelocity('x')
        x -= player.xspeed * dt
    if keys[pygame.K_d]:
        x += player.xspeed * dt
    player.set_pos(x,y)


    if keys[pygame.K_k]:
        player = Player(screen, cam, (x,y), "art/duckSwing.png",(v_x,v_y))
        



        
    pygame.display.flip()

    dt = clock.tick(60) / 1000


