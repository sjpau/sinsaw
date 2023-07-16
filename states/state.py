import pygame
import defs.finals as finals
import defs.screen as s


class State(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.theme = ""
        self.start_playing_music = True
        self.desired_next_state = ""
        self.state_arg = 0
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 50)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def manage_music(self):
        if self.start_playing_music and self.theme != "":
            pygame.mixer.music.load(finals.music_path + self.theme)
            pygame.mixer.music.play(-1)
            self.start_playing_music = False

    def on_enter(self):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass