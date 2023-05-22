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
### PLAYER DEFAULT ###
sprite_path = 'asset/sprites/player/default/attack/'
anim_player_default_attack = [
    sprite_path + 'sprite_player_default_attack_1.png',
    sprite_path + 'sprite_player_default_attack_2.png',
    sprite_path + 'sprite_player_default_attack_3.png',
    sprite_path + 'sprite_player_default_attack_4.png',
    sprite_path + 'sprite_player_default_attack_5.png',
    sprite_path + 'sprite_player_default_attack_6.png',
]
sprite_path = 'asset/sprites/player/default/idle/'
anim_player_default_idle = [
    sprite_path + 'sprite_player_default_idle_1.png',
    sprite_path + 'sprite_player_default_idle_2.png',
    sprite_path + 'sprite_player_default_idle_3.png',
    sprite_path + 'sprite_player_default_idle_4.png',
    sprite_path + 'sprite_player_default_idle_5.png',
]
sprite_path = 'asset/sprites/player/default/smoking/'
anim_player_default_smoking = [
    sprite_path + 'sprite_player_default_smoking_1.png',
    sprite_path + 'sprite_player_default_smoking_2.png',
    sprite_path + 'sprite_player_default_smoking_3.png',
    sprite_path + 'sprite_player_default_smoking_4.png',
    sprite_path + 'sprite_player_default_smoking_5.png',
    sprite_path + 'sprite_player_default_smoking_6.png',
    sprite_path + 'sprite_player_default_smoking_7.png',
    sprite_path + 'sprite_player_default_smoking_8.png',
    sprite_path + 'sprite_player_default_smoking_9.png',
    sprite_path + 'sprite_player_default_smoking_10.png',
    sprite_path + 'sprite_player_default_smoking_11.png',
    sprite_path + 'sprite_player_default_smoking_12.png',
    sprite_path + 'sprite_player_default_smoking_13.png',
    sprite_path + 'sprite_player_default_smoking_14.png',
    sprite_path + 'sprite_player_default_smoking_15.png',
    sprite_path + 'sprite_player_default_smoking_16.png',
    sprite_path + 'sprite_player_default_smoking_17.png',
    sprite_path + 'sprite_player_default_smoking_18.png',
]
sprite_path = 'asset/sprites/player/default/walk/'
anim_player_default_walk = [
    sprite_path + 'sprite_player_default_walk_1.png',
    sprite_path + 'sprite_player_default_walk_2.png',
]

### PLAYER EXTING ###
sprite_path = 'asset/sprites/player/exting/idle/'
anim_player_exting_idle = [
    sprite_path + 'sprite_player_exting_idle_1.png',
    sprite_path + 'sprite_player_exting_idle_2.png',
    sprite_path + 'sprite_player_exting_idle_3.png',
    sprite_path + 'sprite_player_exting_idle_4.png',
]
sprite_path = 'asset/sprites/player/exting/walk/'
anim_player_exting_walk = [
    sprite_path + 'sprite_player_exting_walk_1.png',
    sprite_path + 'sprite_player_exting_walk_2.png',
]

### PLAYER GUN ###
sprite_path = 'asset/sprites/player/gun/attack/'
anim_player_gun_attack = [
    sprite_path + 'sprite_player_gun_attack_1.png',
    sprite_path + 'sprite_player_gun_attack_2.png',
    sprite_path + 'sprite_player_gun_attack_3.png',
    sprite_path + 'sprite_player_gun_attack_4.png',
    sprite_path + 'sprite_player_gun_attack_5.png',
    sprite_path + 'sprite_player_gun_attack_6.png',
    sprite_path + 'sprite_player_gun_attack_7.png',
    sprite_path + 'sprite_player_gun_attack_8.png',
]
sprite_path = 'asset/sprites/player/gun/idle/'
anim_player_gun_idle = [
    sprite_path + 'sprite_player_gun_idle_1.png',
    sprite_path + 'sprite_player_gun_idle_2.png',
]
sprite_path = 'asset/sprites/player/gun/walk/'
anim_player_gun_walk = [
    sprite_path + 'sprite_player_gun_walk_1.png',
    sprite_path + 'sprite_player_gun_walk_2.png',
]

### PLAYER KNIFE ###
sprite_path = 'asset/sprites/player/knife/attack/'
anim_player_knife_attack = [
    sprite_path + 'sprite_player_knife_attack_1.png',
    sprite_path + 'sprite_player_knife_attack_2.png',
    sprite_path + 'sprite_player_knife_attack_3.png',
    sprite_path + 'sprite_player_knife_attack_4.png',
    sprite_path + 'sprite_player_knife_attack_5.png',
    sprite_path + 'sprite_player_knife_attack_6.png',
    sprite_path + 'sprite_player_knife_attack_7.png',
]
sprite_path = 'asset/sprites/player/knife/idle/'
anim_player_knife_idle = [
    sprite_path + 'sprite_player_knife_idle_1.png',
    sprite_path + 'sprite_player_knife_idle_2.png',
    sprite_path + 'sprite_player_knife_idle_3.png',
    sprite_path + 'sprite_player_knife_idle_4.png',
    sprite_path + 'sprite_player_knife_idle_5.png',
]
sprite_path = 'asset/sprites/player/knife/walk/'
anim_player_knife_walk = [
    sprite_path + 'sprite_player_knife_walk_1.png',
    sprite_path + 'sprite_player_knife_walk_2.png',
]

### PLAYER MOLOTOW ###
sprite_path = 'asset/sprites/player/molotow/attack/'
anim_player_molotow_attack = [
    sprite_path + 'sprite_player_molotow_attack_1.png',
    sprite_path + 'sprite_player_molotow_attack_2.png',
    sprite_path + 'sprite_player_molotow_attack_3.png',
    sprite_path + 'sprite_player_molotow_attack_4.png',
    sprite_path + 'sprite_player_molotow_attack_5.png',
    sprite_path + 'sprite_player_molotow_attack_6.png',
]
sprite_path = 'asset/sprites/player/molotow/idle/'
anim_player_molotow_idle = [
    sprite_path + 'sprite_player_molotow_idle_1.png',
    sprite_path + 'sprite_player_molotow_idle_2.png',
    sprite_path + 'sprite_player_molotow_idle_3.png',
    sprite_path + 'sprite_player_molotow_idle_4.png',
]
sprite_path = 'asset/sprites/player/molotow/walk/'
anim_player_molotow_walk = [
    sprite_path + 'sprite_player_molotow_walk_1.png',
    sprite_path + 'sprite_player_molotow_walk_2.png',
]

### ENEMY DOG ###
sprite_path = 'asset/sprites/enemy/dog/idle/'
anim_enemy_dog_idle = [
    sprite_path + 'sprite_enemy_dog_idle_1.png',
    sprite_path + 'sprite_enemy_dog_idle_2.png',
    sprite_path + 'sprite_enemy_dog_idle_3.png',
    sprite_path + 'sprite_enemy_dog_idle_4.png',
]
sprite_path = 'asset/sprites/enemy/dog/walk/'
anim_enemy_dog_walk = [
    sprite_path + 'sprite_enemy_dog_walk_1.png',
    sprite_path + 'sprite_enemy_dog_walk_2.png',
]

### ENEMY GUN ###
sprite_path = 'asset/sprites/enemy/gun/attack/'
anim_enemy_gun_attack = [
    sprite_path + 'sprite_enemy_bandit_gun_attack_1.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_2.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_3.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_4.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_5.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_6.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_7.png',
    sprite_path + 'sprite_enemy_bandit_gun_attack_8.png',
]
sprite_path = 'asset/sprites/enemy/gun/idle/'
anim_enemy_gun_idle = [
    sprite_path + 'sprite_enemy_bandit_gun_idle_1.png',
    sprite_path + 'sprite_enemy_bandit_gun_idle_2.png',
]
sprite_path = 'asset/sprites/enemy/gun/walk/'
anim_enemy_gun_walk = [
    sprite_path + 'sprite_enemy_bandit_gun_walk_1.png',
    sprite_path + 'sprite_enemy_bandit_gun_walk_2.png',
]

### ENEMY KNIFE ###
sprite_path = 'asset/sprites/enemy/knife/attack/'
anim_enemy_knife_attack = [
    sprite_path + 'sprite_enemy_bandit_knife_attack_1.png',
    sprite_path + 'sprite_enemy_bandit_knife_attack_2.png',
    sprite_path + 'sprite_enemy_bandit_knife_attack_3.png',
    sprite_path + 'sprite_enemy_bandit_knife_attack_4.png',
    sprite_path + 'sprite_enemy_bandit_knife_attack_5.png',
    sprite_path + 'sprite_enemy_bandit_knife_attack_6.png',
    sprite_path + 'sprite_enemy_bandit_knife_attack_7.png',
]
sprite_path = 'asset/sprites/enemy/knife/idle/'
anim_enemy_knife_idle = [
    sprite_path + 'sprite_enemy_bandit_knife_idle_1.png',
    sprite_path + 'sprite_enemy_bandit_knife_idle_2.png',
    sprite_path + 'sprite_enemy_bandit_knife_idle_3.png',
    sprite_path + 'sprite_enemy_bandit_knife_idle_4.png',
    sprite_path + 'sprite_enemy_bandit_knife_idle_5.png',
]
sprite_path = 'asset/sprites/enemy/knife/walk/'
anim_enemy_knife_walk = [
    sprite_path + 'sprite_enemy_bandit_knife_walk_1.png',
    sprite_path + 'sprite_enemy_bandit_knife_walk_2.png',
]

### ITEMS ###
sprite_path = 'asset/sprites/items/exting/'
anim_items_exting = [
    sprite_path + 'item_exting_1.png',
    sprite_path + 'item_exting_2.png',
    sprite_path + 'item_exting_3.png',
    sprite_path + 'item_exting_4.png',
    sprite_path + 'item_exting_5.png',
    sprite_path + 'item_exting_6.png',
    sprite_path + 'item_exting_7.png',
]
sprite_path = 'asset/sprites/items/gun/'
anim_items_gun = [
    sprite_path + 'item_gun_1.png',
    sprite_path + 'item_gun_2.png',
    sprite_path + 'item_gun_3.png',
    sprite_path + 'item_gun_4.png',
    sprite_path + 'item_gun_5.png',
    sprite_path + 'item_gun_6.png',
    sprite_path + 'item_gun_7.png',
]
sprite_path = 'asset/sprites/items/key/'
anim_items_key = [
    sprite_path + 'item_key_1.png',
    sprite_path + 'item_key_2.png',
    sprite_path + 'item_key_3.png',
    sprite_path + 'item_key_4.png',
    sprite_path + 'item_key_5.png',
    sprite_path + 'item_key_6.png',
    sprite_path + 'item_key_7.png',
]
sprite_path = 'asset/sprites/items/knife/'
anim_items_knife = [
    sprite_path + 'item_knife_1.png',
    sprite_path + 'item_knife_2.png',
    sprite_path + 'item_knife_3.png',
    sprite_path + 'item_knife_4.png',
    sprite_path + 'item_knife_5.png',
    sprite_path + 'item_knife_6.png',
    sprite_path + 'item_knife_7.png',
]
sprite_path = 'asset/sprites/items/molotow/'
anim_items_molotow = [
    sprite_path + 'item_molotow_1.png',
    sprite_path + 'item_molotow_2.png',
    sprite_path + 'item_molotow_3.png',
    sprite_path + 'item_molotow_4.png',
    sprite_path + 'item_molotow_5.png',
    sprite_path + 'item_molotow_6.png',
    sprite_path + 'item_molotow_7.png',
]