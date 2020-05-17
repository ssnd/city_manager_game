import pygame


class TextBox:
    def  __init__(self, surface, text="", align="left", font_size=25):
        self.align = align
        self.text = text
        self.surface = surface
        self.background_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font_size = font_size
        self.position = (0, 0)
        self.width = 0
        self.height = 0
        self.font_family = "arial"
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.text = self.font.render(text, True, self.text_color, self.background_color)
        self.set_align()

    def get_size(self):
        self.width = self.text_rect.width
        self.height = self.text_rect.height

    def set_align(self):
        if self.align == "center":
            self.position = (self.surface.get_width()/2-self.width/2,self.position[1])

    def set_margin_top(self, x):
        self.position = (self.position[0], x)

    def draw(self, text, margin_top=0):
        self.position = (self.position[0], self.position[1]+margin_top)
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.text = self.font.render(text, True, self.text_color, self.background_color)
        self.text_rect = self.text.get_rect()
        self.get_size()
        self.set_align()
        self.surface.blit(self.text, self.position)

    def draw_new_line(self, text, margin_top=0):
        self.position = (self.position[0], self.position[1]+self.font_size+margin_top)
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.text = self.font.render(text, True, self.text_color, self.background_color)
        self.text_rect = self.text.get_rect()
        self.get_size()
        self.set_align()
        self.surface.blit(self.text, self.position)