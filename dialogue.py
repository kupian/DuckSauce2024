import pygame
import yaml
from camera import *

# Source: https://www.pygame.org/wiki/TextWrap#:~:text=Simple%20Text%20Wrapping%20for%20pygame.&text=Simple%20function%20that%20will%20draw,make%20the%20line%20closer%20together.
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
class TextBox:
    def __init__(self, surface, cam:Camera, pos:tuple=None, size:tuple=None):
        self.cam = cam
        WIN_WIDTH, WIN_HEIGHT = self.cam.cam_size
        if not pos:
            pos = ((WIN_WIDTH/10)*2, WIN_HEIGHT-WIN_HEIGHT*0.25)
        if not size:
            size = ((WIN_WIDTH/10)*6, WIN_HEIGHT*0.2)
        self.pos,self.size = pos,size

        self.rect = pygame.Rect(self.pos, self.size)
        self.surface = surface
        self.text = ""

    def wrap_text(self, surface, text, aa=False, bkg=None):
        font = pygame.font.Font('freesansbold.ttf', 14)
        colour = (0,0,0)
        rect = pygame.rect.Rect(self.rect)
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
                image = font.render(text[:i], 1, colour, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, colour)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text

    def set_text(self, text):
        self.text = text

    def draw(self):
        colour = (255,255,255)
        pygame.draw.rect(self.surface, colour, self.rect)
        if self.text:
            text = self.wrap_text(self.surface, self.text)

class WorldSpaceTextBox(TextBox):
    def __init__(self, surface, cam:Camera, pos:tuple=None, size:tuple=None):
        self.cam = cam
        if not pos:
            pos = (0,0)
        if not size:
            size = (200,100)
        self.pos,self.size = pos,size

        self.rect = pygame.Rect(self.pos, self.size)
        self.surface = surface
        self.text = ""

    def draw(self):
        self.rect = self.cam.draw(pos=self.pos, size=self.size)
        self.wrap_text(self.surface, self.text)

class Button(TextBox):
    def __init__(self, surface, cam:Camera, pos:tuple=None, size:tuple=None, on_click=None) -> None:
        super().__init__(surface, cam)
        self.on_click = on_click

class Quest:
    def __init__(self, quest_file) -> None:
        with open(quest_file) as f:
            self.quest = yaml.safe_load(f)
            self.checkpoint = 1
            self.buttons = []

    def add_buttons(self, tbox:TextBox, *args: int):
        button_count = len(args)
        button_width = tbox.size[0]/button_count
        button_height = tbox.size[1]/3
        for i in range(button_count):
            btn = Button(tbox.surface, tbox.cam, (tbox.pos[0]+i*button_width, tbox.pos[1]-button_height), (button_width,button_height))
            self.buttons.append(btn)

    def show_current_dialogue(self, surface:pygame.Surface, cam:Camera) -> TextBox:
        tbox = TextBox(surface, cam)
        tbox.set_text(self.quest["checkpoints"][self.checkpoint]["text"])

        routes = self.quest["checkpoints"][self.checkpoint]["routes"]
        self.add_buttons(tbox, *routes)
        self.buttons.append(tbox)
        
        return self.buttons