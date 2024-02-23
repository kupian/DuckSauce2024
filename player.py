import pygame

class Player:
    def __init__(self, x,y) -> None:
        self.G = 9.8
        self.pos = pygame.Vector2(x,y)
        self.speed = 300
        self.radius = 40

    def set_pos(self, x: float, y: float) -> None:
        x_b,y_b = pygame.display.get_window_size()
        if x <= 0:
            x = 0
        if x >= x_b:
            x = x_b
        if y <= 0:
            y = 0
        if y>= y_b:
            y = y_b   
        self.pos = pygame.Vector2(x,y)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "red", self.pos, self.radius)
    
    def gravity(self,x: float,y: float,terrian: bool) -> None:
        if terrian is True:
            pass
        else:
            pass