import pygame
from dialogue import TextBox, Button, WorldSpaceTextBox
import spriteSheet
from camera import Camera
from sprites import *
import numpy as np

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
x,y = LEVEL_SIZE
x /=2
y/=2
v_x = 0
v_y = 1
# Used for animations WIP
timing = False

bg=Sprite(screen, cam, (0,0), "art/bgtest2.png")

player = Player(screen, cam, (x,y),"art/static_duck.png",(v_x,v_y))

npc = NPC(screen, cam, (x,y), "art/scientist.png")
npc.set_quest("quests/intro.yaml")

key_guide = WorldSpaceTextBox(screen, cam, (x-100,y), (100,50))
key_guide.set_text("Keys: K - Attack, F - Interact")

gui = []
i=0
swing=False

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

    screen.fill("white")

    # Testing object
    obj_pos = (20,20)
    bg.draw()
    player.draw()
    npc.draw()


    for gui_item in gui:
        gui_item.draw()
    key_guide.draw()

    # Draw object with camera. Object should be converted to a sprite object and draw called that way
    # instead of directly on the camera
    cam.draw(pos=obj_pos)
    

    # TODO: Cleanup velocity / gravity code and move functions inside of player class for readability
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        gui = []
        for gui_item in npc.talk():
            gui.append(gui_item)

    x,y = player.pos
    v_y -= player.G
    if v_y > 5:
        v_y = 5
    player.setVelocity((v_x,v_y))
    y += player.getVelocity('y')
    if not keys[pygame.K_w]:
        wKeyDown=False
    if keys[pygame.K_w]:
        if wKeyDown == False:
            v_y = -player.yspeed
            player.setVelocity((v_x,v_y))
        wKeyDown=True
    

    if keys[pygame.K_s]:
        y += player.yspeed * dt
    if keys[pygame.K_a]:
        player.getVelocity('x')
        #player = Player(screen, cam, (x,y), "art/static_duck.png",(v_x,v_y))
        player.set_frame("art/static_duck.png")
        x -= player.xspeed * dt
        if not swing:
            animImage = pygame.image.load("art/walkLeft.png")

            frame0=spriteSheet.get_image(animImage,i,32)
            pygame.image.save(frame0,"art/currentFrame.png")
            player.set_frame("art/currentFrame.png")
            i+=1
            if i>9:
                i=0
    if keys[pygame.K_d]:
        x += player.xspeed * dt
        #player = Player(screen, cam, (x,y), "art/staticDuckRight.png",(v_x,v_y))
        if not swing:
            player.set_frame("art/staticDuckRight.png")
            
            animImage = pygame.image.load("art/walkRight.png")

            frame0=spriteSheet.get_image(animImage,i,32)
            pygame.image.save(frame0,"art/currentFrame.png")
            player.set_frame("art/currentFrame.png")
            i+=1
            if i>9:
                i=0
    player.set_pos(pygame.Vector2(x,y))

    if keys[pygame.K_k]:
        swing=True
    
    if swing:
        animImage = pygame.image.load("art/spriteSheetRow.png")

        frame0=spriteSheet.get_image(animImage,i,32)
        pygame.image.save(frame0,"art/currentFrame.png")
        player.set_frame("art/currentFrame.png")
        i+=1
        if i>20:
            i=0
            swing=False
        
    pygame.display.flip()

    dt = clock.tick(60) / 1000


