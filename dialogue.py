import pygame

# Source: https://www.pygame.org/wiki/TextWrap#:~:text=Simple%20Text%20Wrapping%20for%20pygame.&text=Simple%20function%20that%20will%20draw,make%20the%20line%20closer%20together.
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def draw_text(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

class DialogueBox:
    def __init__(self, surface, colour=(255,255,255), pos:tuple=None, size:tuple=None):
        WIN_WIDTH,WIN_HEIGHT = pygame.display.get_window_size()

        if not pos:
            pos = ((WIN_WIDTH/10)*2, WIN_HEIGHT-WIN_HEIGHT*0.25)
        if not size:
            size = ((WIN_WIDTH/10)*6, WIN_HEIGHT*0.2)
        self.pos,self.size = pos,size

        self.rect = pygame.Rect(self.pos, self.size)
        self.surface = surface
        self.colour = colour

    def write(self, text):
        pygame.draw.rect(self.surface, self.colour, self.rect)
        font = pygame.font.Font('freesansbold.ttf', 16)
        draw_text(self.surface, text, (0,0,0), self.rect, font)

    def set_routes(self, *args: int):
        route_count = len(args)
        route_width = self.size[0]/route_count
        route_height = self.size[1]/3
        for i in range(route_count):
            rect = pygame.Rect(i*route_width,0, route_width, route_height)
            pygame.draw.rect(self.surface, self.colour, rect)

class Button(DialogueBox):
    def __init__(self, surface, colour=(255,255,255), on_click:function=None) -> None:
        super().__init__(surface, colour)
        self.on_click = on_click


        