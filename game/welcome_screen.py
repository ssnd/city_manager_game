from pygame.surface import Surface
from game import config as CONFIG
from game.utils.text_box import TextBox


class WelcomeScreen(object):
    def __init__(self, mouse):
        self.mouse = mouse
        self.surface_size = (CONFIG['screen']['width']/2, CONFIG['screen']['height']/2)
        self.surface = Surface(self.surface_size)

    def draw(self, screen):
        text_box = TextBox(self.surface, align="center")
        self.surface.fill((0,175,75))
        text_box.text_color = (32, 32, 32)
        text_box.background_color = ((0, 175, 75))
        text_box.font_size = 35
        text_box.draw_new_line("Welcome to the", margin_top=-20)
        text_box.draw_new_line("City Manager Game!")

        text_box.font_size = 25
        text_box.draw_new_line("Here you can create new buildings, roads", margin_top=20)
        text_box.draw_new_line("and earn money from the things you have built.")
        text_box.draw_new_line(f"Every {CONFIG['income_period']/1000} seconds you will earn money", margin_top=5)
        text_box.draw_new_line("from your belongings.")
        text_box.draw_new_line("You can build new things using the ")
        text_box.draw_new_line("money you have as well.")
        text_box.draw_new_line("Have fun!")
        text_box.draw_new_line("Press enter to continue", margin_top=10)

        screen.blit(self.surface, (self.surface_size[0]/2,
                                   self.surface_size[1]/2))

