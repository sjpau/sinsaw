from typing import Final
import pygame
from entity.animation import Animation
import loader.anims as anims
import loader.asset as asset
pygame.mixer.init()

tile_size: Final = 64
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
    #'example.json',
    'chapter_night_shift/the_night_shift_1.json',
    'chapter_night_shift/the_night_shift_2.json',
    'chapter_night_shift/the_night_shift_3.json',
    'chapter_night_shift/the_night_shift_4.json',
    'chapter_night_shift/the_night_shift_5.json',
    ]

chapters: Final = {
    'The Night Shift': chapter_night_shift,
}

anim_default_attack, anim_default_idle, anim_default_smoking, anim_default_walk = anims.load_animations_player_default()
anim_molotow_attack, anim_molotow_idle,  anim_molotow_walk = anims.load_animations_player_molotow()
anim_exting_idle,  anim_exting_walk = anims.load_animations_player_exting()
anim_knife_attack, anim_knife_idle,  anim_knife_walk = anims.load_animations_player_knife()
anim_gun_attack, anim_gun_idle,  anim_gun_walk = anims.load_animations_player_gun()
animations_player = {
    'default_attack': Animation(anim_default_attack, 100),
    'default_idle': Animation(anim_default_idle, 300),
    'default_smoking': Animation(anim_default_smoking, 300),
    'molotow_attack': Animation(anim_molotow_attack, 200),
    'molotow_idle': Animation(anim_molotow_idle, 300),
    'molotow_walk': Animation(anim_molotow_walk, 100),
    'exting_idle': Animation(anim_exting_idle, 300),
    'exting_walk': Animation(anim_exting_idle, 100),
    'knife_attack': Animation(anim_knife_attack, 200),
    'knife_idle': Animation(anim_knife_idle, 300),
    'knife_walk': Animation(anim_knife_walk, 100),
    'gun_attack': Animation(anim_gun_attack, 200),
    'gun_idle': Animation(anim_gun_idle, 300),
    'gun_walk': Animation(anim_gun_idle, 100),
}
anim_exting = anims.load_animation_item_exting()
animations_exting = {
  'anim': Animation(anim_exting, 200)
}
anim_gun = anims.load_animation_item_gun()
animations_gun = {
  'anim': Animation(anim_gun, 200)
}
anim_knife = anims.load_animation_item_knife()
animations_knife = {
  'anim': Animation(anim_knife, 200)
}
anim_molotow = anims.load_animation_item_molotow()
animations_molotow = {
  'anim': Animation(anim_molotow, 200)
}
anim_key = anims.load_animation_item_key()
animations_key = {
  'anim': Animation(anim_key, 200)
}
sprites_attack, sprites_idle, sprites_walk = anims.load_animation_enemy_knife()
animations_enemy_knife = {
    'idle': Animation(sprites_idle, 300),
    'attack': Animation(sprites_attack, 200),
    'walk': Animation(sprites_walk, 100),
}
sprites_attack, sprites_idle, sprites_walk = anims.load_animation_enemy_gun()
animations_enemy_gun = {
    'idle': Animation(sprites_idle, 500),
    'attack': Animation(sprites_attack, 200),
    'walk': Animation(sprites_walk, 100),
}
sprites_idle, sprites_walk = anims.load_animation_enemy_dog()
animations_enemy_dog = {
    'idle': Animation(sprites_idle, 300),
    'walk': Animation(sprites_walk, 100),
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

### MISC ###
image_door_broken_1 = pygame.image.load(asset.door_broken_1).convert_alpha()
image_door_broken_1 = pygame.transform.scale(image_door_broken_1, (tile_size, tile_size))
image_door_broken_2 = pygame.image.load(asset.door_broken_2).convert_alpha()
image_door_broken_2 = pygame.transform.scale(image_door_broken_2, (tile_size, tile_size))
image_door_unlocked_1 = pygame.image.load(asset.door_unlocked_1).convert_alpha()
image_door_unlocked_1 = pygame.transform.scale(image_door_unlocked_1, (tile_size, tile_size))
image_door_unlocked_2 = pygame.image.load(asset.door_unlocked_2).convert_alpha()
image_door_unlocked_2 = pygame.transform.scale(image_door_unlocked_2, (tile_size, tile_size))