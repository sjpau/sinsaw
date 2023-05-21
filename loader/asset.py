import pygame

static_path = "asset/static/"
sprite_path = "asset/sprites/"

image_player_default = sprite_path + "sprite_player_default_1.png"
image_player_gun = sprite_path + "sprite_player_gun_1.png"
image_enemy_dog = sprite_path + "sprite_enemy_dog_1.png"
image_enemy_gun = sprite_path + "sprite_enemy_gun_1.png"
image_enemy_knife = sprite_path + "sprite_enemy_knife_1.png"
item_gun = static_path + "item_gun.png"
item_molotow = static_path + "item_molotow.png"
item_exting = static_path + "item_exting.png"
item_knife = static_path + "item_knife.png"
item_key = static_path + "item_key.png"
floor_0 = "floor_0.png"
floor_1 = "floor_1.png"
floor_2 = "floor_2.png"
wall_1 = "wall_1.png"
door_1 = "door_1.png"
door_2 = "door_2.png"
door_locked_1 = "door_locked_1.png"
door_locked_2 = "door_locked_2.png"
glass_1 = "glass_1.png"
glass_2 = "glass_2.png"

tileset = {
    "0": floor_1,
    "9": floor_0,
    "8": floor_2,
    "1": wall_1,
    "2": door_1,
    "3": door_2,
    "4": glass_1,
    "5": glass_2,
    "6": door_locked_1,
    "7": door_locked_2
}