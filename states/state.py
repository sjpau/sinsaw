import pygame
import defs.screen as s


class State(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.desired_next_state = ""
        self.state_arg = 0
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 50)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass