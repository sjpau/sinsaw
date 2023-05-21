import pygame
import finals
from .state import State


class Splash(State):
    def __init__(self, surface):
        super(Splash, self).__init__()
        self.surface = surface
        self.title = self.font.render("This is a testing environment.\nEverything you see is subject to change.", True, finals.COLOR_PURPLE)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 2000:
            self.done = True
    
    def get_event(self, event):
        if event.type == pygame.VIDEORESIZE:
            if not self.fullscreen:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.surface = pygame.display.set_mode((self.surface.get_width(), self.surface.get_height()), pygame.FULLSCREEN)
                else:
                    self.surface = pygame.display.set_mode((self.surface.get_width(), self.surface.get_height()), pygame.RESIZABLE)

    def draw(self):
        self.surface.fill(finals.COLOR_BLACK)
        self.surface.blit(self.title, self.title_rect)