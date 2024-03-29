import pygame
from dialogue import TextBox, Button, WorldSpaceTextBox
import spriteSheet
from camera import Camera
from sprites import *
import numpy as np
import math

## no thanks to alex we have arrived at the game jam
## going to lose :)


CAMERA_SIZE = (460,256)
LEVEL_SIZE = (2560,1440)

pygame.init()

flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(CAMERA_SIZE, flags)
cam = Camera(screen, CAMERA_SIZE, LEVEL_SIZE)

clock = pygame.time.Clock()
running = True

dt = 0
timer = 0
player_start = (LEVEL_SIZE[0]/2, LEVEL_SIZE[1]/2)
# Used for animations WIP
timing = False

pygame.mixer.init()
pygame.mixer.music.load("art/BeepBox-Song.wav")
pygame.mixer.music.play(-1)


bg=Sprite(screen, cam, (0,0), "art/bgtest2.png")

player = Player(screen, cam, player_start,"art/static_duck.png")
enemy = Enemy(screen, cam, (player_start[0]+50, player_start[1]), "art/scientist.png", player)

npc = NPC(screen, cam, player_start, "art/scientist.png")
npc.set_quest("quests/intro.yaml")

key_guide = WorldSpaceTextBox(screen, cam, (player_start[0]-100,player_start[1]), (100,50))
key_guide.set_text("Keys: K - Attack, F - Interact")

gui = []
i=0
swing= False
downTrue= False
jump_key_pressed = False

while running:
    if timing:
        timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # HANDLE GUI CLICKS
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for gui_item in gui:
                if type(gui_item) == Button:
                    if gui_item.rect.collidepoint(mouse_pos):
                        try:
                            gui_item.on_click()
                        except AttributeError as e:
                            print("Button has no click function defined")

        if event.type == pygame.KEYUP:
            player.set_speed(0)

            if event.key == pygame.K_w:
                jump_key_pressed = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.set_speed(-1)
        if not swing:
            animImage = pygame.image.load("art/walkLeft.png")

            frame=spriteSheet.get_image(animImage,i%9,32)
            #pygame.image.save(frame0,"art/currentFrame.png")
            player.set_frame(image=frame)

    if keys[pygame.K_d]:
        player.set_speed(1)
        if not swing:
            player.set_frame("art/staticDuckRight.png")

            animImage = pygame.image.load("art/walkRight.png")

            frame=spriteSheet.get_image(animImage,i%9,32)
            player.set_frame(image=frame)

    if keys[pygame.K_w]:
        player.jump()
        
        image = pygame.image.load("art/fly.png")
        frame=spriteSheet.get_image(image,i%16,32)
        player.set_frame(image=frame)

    if keys[pygame.K_s]:
        image = pygame.image.load("art/flyDown.png")
        player.set_frame(image=image)
        if player.velocity[1] < 0:
            player.velocity[1] = -player.speed[1]
        else:
            player.velocity[1] = pygame.math.clamp(player.velocity[1]-player.speed[1]*dt, -10, 10)
        downTrue=True

    if keys[pygame.K_k]:
        swing=True
        enemy.hit(10)
        image = pygame.image.load("art/spritesheetRow.png")
        frame0=spriteSheet.get_image(image,i,32)
        pygame.image.save(frame0,"art/currentFrame.png")
        player.set_frame("art/currentFrame.png")
        i+=1
        if i>16:    
            i=0

    screen.fill("white")

    # Testing object
    bg.draw()
    npc.draw()

    for gui_item in gui:
        gui_item.draw()
    key_guide.draw()

    if keys[pygame.K_f]:
        gui = []
        for gui_item in npc.talk():
            gui.append(gui_item)     

    downTrue=False
    
    if swing:
        animImage = pygame.image.load("art/spriteSheetRow.png")

        frame0=spriteSheet.get_image(animImage,i%20,32)
        pygame.image.save(frame0,"art/currentFrame.png")
        player.set_frame("art/currentFrame.png")
        if i>20:
            swing=False

    player.update(dt)
    player.draw()

    enemy.move(dt)
    enemy.draw()
    pygame.display.flip()
    dt = clock.tick(24) / 1000
    i += 1

#update for merge
