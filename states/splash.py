import pygame
from .state import State


class Splash(State):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("Sinsaw", True, pygame.Color("White"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 2000:
            self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)