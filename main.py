import pygame
from player import Player
from dialogue import DialogueBox
import spriteSheet

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

bg=Player(screen,"art/test_bg.png",x,y)
player = Player(screen,"art/static_duck.png", x, y)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box = DialogueBox(screen)
    box.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
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
        ss = spriteSheet.spritesheet('art/duckSwing.png')
        image = ss.image_at((0, 0, 32, 32))
        images = []
        images = ss.images_at((0, 0, 16, 16),(33, 33, 16,16), colorkey=(255, 255, 255))
        
        pygame.display.flip()

    dt = clock.tick(60) / 1000


