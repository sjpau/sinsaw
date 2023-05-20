import pygame
import finals
from .state import State


class Splash(State):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("This is a testing environment.\nEverything you see is subject to change.", True, finals.COLOR_PURPLE)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 2000:
            self.done = True

    def draw(self, surface):
        surface.fill(finals.COLOR_BLACK)
        surface.blit(self.title, self.title_rect)