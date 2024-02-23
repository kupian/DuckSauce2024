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
    def __init__(self, surface, colour=(255,255,255)):
        WIN_WIDTH,WIN_HEIGHT = pygame.display.get_window_size()
        rect = pygame.Rect((WIN_WIDTH/10)*2, WIN_HEIGHT-180, (WIN_WIDTH/10)*6, 150)
        self.surface = surface
        self.colour = colour
        self.rect = pygame.Rect(rect)

    def write(self, text):
        pygame.draw.rect(self.surface, self.colour, self.rect)
        font = pygame.font.Font('freesansbold.ttf', 32)
        draw_text(self.surface, text, (0,0,0), self.rect, font)
