import pygame
from .state import State
import defs.finals as finals


class Menu(State):
    def __init__(self):
        super(Menu, self).__init__()
        self.surface = pygame.display.get_surface()
        self.active_index = 0
        self.levels = {
            "The Night Shift": 1, 
            "The Afterparty": 2,
        }
        self.levels_keys = list(self.levels.keys())
        self.choose_level = "< " + self.levels_keys[0] + " >"
        self.options = ["Start Game", self.choose_level, "Quit Game"]
        self.chosen_level = self.levels[self.levels_keys[0]]
        self.next_state = ""

    def render_text(self, index):
        color = finals.COLOR_BEIGE if index == self.active_index else finals.COLOR_PINK
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.centerx, self.screen_rect.centery + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            if self.chosen_level == 1:
                self.next_state = 'CHAPTER_NIGHT_SHIFT'
            elif self.chosen_level == 2:
                self.next_state = 'CHAPTER_AFTERPARTY'
            self.done = True
        elif self.active_index == 1:
            pass
        elif self.active_index == 2:
            self.quit = True
    
    def switch_levels(self):
        current_level_index = self.levels_keys.index(self.choose_level[2:-2])
        new_level_index = (current_level_index - 1) % len(self.levels_keys)
        self.choose_level = "< " + self.levels_keys[new_level_index] + " >"
        self.options = ["Start Game", self.choose_level, "Quit Game"]
        self.chosen_level = self.levels[self.levels_keys[new_level_index]]
        self.state_arg = self.chosen_level

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.VIDEORESIZE:
            if not self.fullscreen:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.screen_rect = pygame.display.get_surface().get_rect()
            else:
                self.screen_rect = pygame.display.get_surface().get_rect()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.surface = pygame.display.set_mode((self.surface.get_width(), self.surface.get_height()), pygame.FULLSCREEN)
                else:
                    self.surface = pygame.display.set_mode((self.surface.get_width(), self.surface.get_height()), pygame.RESIZABLE)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.active_index = (self.active_index - 1) % len(self.options)
                finals.sfx_menu_click.play()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.active_index = (self.active_index + 1) % len(self.options)
                finals.sfx_menu_click.play()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if self.active_index == 1:
                    self.switch_levels()
                    finals.sfx_menu_click.play()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if self.active_index == 1:
                    self.switch_levels()
                    finals.sfx_menu_click.play()
            elif event.key == pygame.K_RETURN:
                self.handle_action()
                finals.sfx_menu_click.play()

  

    def draw(self):
        self.surface.fill(finals.COLOR_BLACK)
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            self.surface.blit(text_render, self.get_text_position(text_render, index))
    