import pygame
from player import Player

## no thanks to alex we have arrived at the game jam
## going to lose :)

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

dt = 0

player = Player(100, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    player.draw(screen)

    keys = pygame.key.get_pressed()
    x,y = player.pos
    if keys[pygame.K_w]:
        y -= 300 * dt
    if keys[pygame.K_s]:
        y += 300 * dt
    if keys[pygame.K_a]:
        x -= 300 * dt
    if keys[pygame.K_d]:
        x += 600 * dt
    player.set_pos(x,y)

    pygame.display.flip()

    dt = clock.tick(60) / 1000


# right is now faster