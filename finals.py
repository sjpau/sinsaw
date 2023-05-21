from typing import Final
import pygame
pygame.mixer.init()

COLOR_BLACK: Final = pygame.Color((16, 13, 19))
COLOR_PURPLE: Final = pygame.Color((74, 36, 128))
COLOR_PINK: Final = pygame.Color((197, 58, 157))
COLOR_BEIGE: Final = pygame.Color((255, 142, 128))
COLOR_RED: Final = pygame.Color((255, 0, 0))
COLOR_RED_SUBTLE: Final = pygame.Color((170, 61, 57))
COLOR_ORANGE: Final = pygame.Color((255, 143, 0))
COLOR_GREY: Final = pygame.Color((149, 165, 166))
COLOR_GREY_DARK: Final = pygame.Color((20, 20, 20))

chapter_night_shift: Final = [
  #  'example.json',
    'chapter_night_shift/the_night_shift_1.json',
    'chapter_night_shift/the_night_shift_2.json',
    'chapter_night_shift/the_night_shift_3.json'
    ]

chapters: Final = {
    'The Night Shift': chapter_night_shift,
}

music_path: Final = 'asset/sound/music/'
sfx_path: Final = 'asset/sound/sfx/'
sfx_bottle_break: Final = pygame.mixer.Sound(sfx_path + 'bottle_break.ogg')
sfx_door_break_1: Final = pygame.mixer.Sound(sfx_path + 'door_break_1.ogg')
sfx_door_break_2: Final = pygame.mixer.Sound(sfx_path + 'door_break_2.ogg')
sfx_explode: Final = pygame.mixer.Sound(sfx_path + 'explode.ogg')
sfx_fire: Final = pygame.mixer.Sound(sfx_path + 'fire.ogg')
sfx_flame: Final = pygame.mixer.Sound(sfx_path + 'flame.ogg')
sfx_gun_pickup: Final = pygame.mixer.Sound(sfx_path + 'gun_pickup.ogg')
sfx_knife_pickup: Final = pygame.mixer.Sound(sfx_path + 'knife_pickup.ogg')
sfx_menu_click: Final = pygame.mixer.Sound(sfx_path + 'menu_click.ogg')
sfx_molotow_pickup: Final = pygame.mixer.Sound(sfx_path + 'molotow_pickup.ogg')
sfx_steam: Final = pygame.mixer.Sound(sfx_path + 'steam.ogg')
sfx_shoot: Final = pygame.mixer.Sound(sfx_path + 'shoot.ogg')
sfx_shoot_enemy: Final = pygame.mixer.Sound(sfx_path + 'shoot_enemy.ogg')
sfx_key_pickup: Final = pygame.mixer.Sound(sfx_path + 'key_pickup.ogg')
sfx_ext_pickup: Final = pygame.mixer.Sound(sfx_path + 'ext_pickup.ogg')
sfx_step: Final = pygame.mixer.Sound(sfx_path + 'step.ogg')
sfx_door_on_shot: Final = pygame.mixer.Sound(sfx_path + 'door_on_shot.ogg')
sfx_glass_on_shot: Final = pygame.mixer.Sound(sfx_path + 'glass_on_shot.ogg')
sfx_knife_stab: Final = pygame.mixer.Sound(sfx_path + 'knife_stab.ogg')
sfx_scream_1: Final = pygame.mixer.Sound(sfx_path + 'scream_1.ogg')
sfx_scream_2: Final = pygame.mixer.Sound(sfx_path + 'scream_2.ogg')
sfx_scream_3: Final = pygame.mixer.Sound(sfx_path + 'scream_3.ogg')
sfx_scream: Final = [sfx_scream_1, sfx_scream_2, sfx_scream_3]
sfx_step.set_volume(0.3)
sfx_glass_on_shot.set_volume(0.3)
sfx_door_on_shot.set_volume(0.3)