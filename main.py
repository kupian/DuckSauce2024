import pygame
from player import Player
from dialogue import DialogueBox

## no thanks to alex we have arrived at the game jam
## going to lose :)

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

dt = 0
x,y = pygame.display.get_window_size()
x /=2
y/=2

player = Player(screen, "art/static_duck.png", x, y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("blue")

    box = DialogueBox(screen)
    box.draw()

    player.draw()

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