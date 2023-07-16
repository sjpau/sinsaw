import pygame
from .state import State
import defs.finals as finals
import loader.save as save
import loader.anims as anims

class Menu(State):
    def __init__(self, theme=""):
        super(Menu, self).__init__()
        self.surface = pygame.display.get_surface()
        self.theme = theme
        self.active_index = 0
        self.lock = False
        self.levels = {
            "Night Shift": 1, 
            "The Afterparty": 2,
            "Carte Blanche": 3,
        }
        self.display_achievements = {
            "Night Shift": 0,
            "The Afterparty": -1,
            "Carte Blanche": -1,
        }
        images_skulls = anims.load_skulls()
        self.skulls = []
        for img in images_skulls:
            img = pygame.transform.scale(img, (finals.tile_size/2, finals.tile_size/2))
            self.skulls.append(img) 
        self.available_levels = [1]
        self.levels_keys = list(self.levels.keys())
        self.choose_level = "< " + self.levels_keys[0] + " >"
        self.options = ["Start Game", self.choose_level, "Quit Game"]
        self.chosen_level = self.levels[self.levels_keys[0]]
        self.chosen_level_name = "Night Shift"
        self.next_state = ""

    def render_text(self, index):
        color = finals.COLOR_BEIGE if index == self.active_index else finals.COLOR_PINK
        if self.display_achievements[self.chosen_level_name] == -1 and index == 0:
            color = finals.COLOR_GREY
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
            elif self.chosen_level == 3:
                self.next_state = 'CHAPTER_CARTE_BLANCHE'
            if not self.lock:
                self.done = True
        elif self.active_index == 1:
            pass
        elif self.active_index == 2:
            self.quit = True
    
    def switch_levels(self, reverse=False):
        current_level_index = self.levels_keys.index(self.choose_level[2:-2])
        if reverse:
            new_level_index = (current_level_index - 1) % len(self.levels_keys)
        else:
            new_level_index = (current_level_index + 1) % len(self.levels_keys)
        self.choose_level = "< " + self.levels_keys[new_level_index] + " >"
        self.options = ["Start Game", self.choose_level, "Quit Game"]
        self.chosen_level_name = self.levels_keys[new_level_index]
        self.chosen_level = self.levels[self.chosen_level_name]
        if self.display_achievements[self.chosen_level_name] == -1:
            self.lock = True
        else:
            self.lock = False
        self.state_arg = self.chosen_level

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.VIDEORESIZE:
            self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            self.screen_rect = pygame.display.get_surface().get_rect()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.active_index = (self.active_index - 1) % len(self.options)
                finals.sfx_menu_click.play()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.active_index = (self.active_index + 1) % len(self.options)
                finals.sfx_menu_click.play()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if self.active_index == 1:
                    self.switch_levels(True)
                    finals.sfx_menu_click.play()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if self.active_index == 1:
                    self.switch_levels()
                    finals.sfx_menu_click.play()
            elif event.key == pygame.K_RETURN:
                self.handle_action()
                finals.sfx_menu_click.play()

    def on_enter(self):
        save.load_game_data()
        # 2am workaround dont judge me
        if save.game_save['Night Shift']['Completed'] is True:
            self.display_achievements['The Afterparty'] = 0
        if save.game_save['The Afterparty']['Completed'] is True:
            self.display_achievements['Carte Blanche'] = 0
        for i in self.levels:
            lvl = save.game_save[i]
            z = 0
            for _, value in lvl.items():
                if value == True:
                    z += 1
            if self.display_achievements[i] != -1:
                self.display_achievements[i] = z

        

    def update(self, dt):
        self.manage_music()

    def draw(self):
        self.surface.fill(finals.COLOR_BLACK)
        first_text_rect = self.get_text_position(self.render_text(0), 0)
        num_skulls = self.display_achievements[self.chosen_level_name]
        if num_skulls == 3:
            ach_img = self.skulls[1]
        else:
            ach_img = self.skulls[0]
        if num_skulls != -1:
            y_offset = 0
            for _ in range(num_skulls):
                self.surface.blit(ach_img, (first_text_rect.center[0] - ach_img.get_width()/2, first_text_rect.center[1] - 70 - y_offset))
                y_offset += ach_img.get_height() + 10
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            self.surface.blit(text_render, self.get_text_position(text_render, index))
    