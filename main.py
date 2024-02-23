import pygame
from player import Player
from dialogue import DialogueBox
from camera import Camera
## no thanks to alex we have arrived at the game jam
## going to lose :)

CAMERA_SIZE = (460,256)
LEVEL_SIZE = (2560,1440)

pygame.init()
screen = pygame.display.set_mode(CAMERA_SIZE)

clock = pygame.time.Clock()
running = True

dt = 0
x,y = pygame.display.get_window_size()
x /=2
y/=2

cam = Camera(CAMERA_SIZE, LEVEL_SIZE)
player = Player(screen, cam, "art/static_duck.png", (x,y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("blue")

    #box = DialogueBox(screen)
    #box.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    player.draw()
    obj_pos = (600,100)
    obj_size = (50,50)
    obj_rect = pygame.rect.Rect(cam.local_pos(obj_pos), cam.local_size(obj_size))
    pygame.draw.rect(screen, (255,0,0), obj_rect)

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

    pygame.display.flip()

    dt = clock.tick(60) / 1000


# right is now faster