import pygame
import loader.asset as asset

anim_molotow_attack = None
anim_molotow_idle = None
anim_molotow_walk = None
def load_animations_player_molotow():
    global anim_molotow_attack, anim_molotow_idle, anim_molotow_walk

    if anim_molotow_attack is None: #It was 4am and I am not sure why I did this. not gonna fix ofcourse
        anim_molotow_attack = []
        for path in asset.anim_player_molotow_attack:
            image = pygame.image.load(path).convert_alpha()
            anim_molotow_attack.append(image)
    if anim_molotow_walk is None: 
        anim_molotow_walk = []
        for path in asset.anim_player_molotow_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_molotow_walk.append(image)
    if anim_molotow_idle is None:
        anim_molotow_idle = []
        for path in asset.anim_player_molotow_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_molotow_idle.append(image)
    return anim_molotow_attack, anim_molotow_idle, anim_molotow_walk

anim_default_attack = None
anim_default_idle = None
anim_default_smoking = None
anim_default_walk = None

def load_animations_player_default():
    global anim_default_attack, anim_default_idle, anim_default_smoking, anim_default_walk

    if anim_default_attack is None:
        anim_default_attack = []
        for path in asset.anim_player_default_attack:
            image = pygame.image.load(path).convert_alpha()
            anim_default_attack.append(image)

    if anim_default_idle is None:
        anim_default_idle = []
        for path in asset.anim_player_default_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_default_idle.append(image)

    if anim_default_smoking is None:
        anim_default_smoking = []
        for path in asset.anim_player_default_smoking:
            image = pygame.image.load(path).convert_alpha()
            anim_default_smoking.append(image)

    if anim_default_walk is None:
        anim_default_walk = []
        for path in asset.anim_player_default_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_default_walk.append(image)

    return anim_default_attack, anim_default_idle, anim_default_smoking, anim_default_walk

anim_exting_idle = None
anim_exting_walk = None

def load_animations_player_exting():
    global anim_exting_idle, anim_exting_walk

    if anim_exting_idle is None:
        anim_exting_idle = []
        for path in asset.anim_player_exting_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_exting_idle.append(image)

    if anim_exting_walk is None:
        anim_exting_walk = []
        for path in asset.anim_player_exting_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_exting_walk.append(image)

    return anim_exting_idle, anim_exting_walk

anim_gun_attack = None
anim_gun_idle = None
anim_gun_walk = None

def load_animations_player_gun():
    global anim_gun_attack, anim_gun_idle, anim_gun_walk

    if anim_gun_attack is None:
        anim_gun_attack = []
        for path in asset.anim_player_gun_attack:
            image = pygame.image.load(path).convert_alpha()
            anim_gun_attack.append(image)

    if anim_gun_idle is None:
        anim_gun_idle = []
        for path in asset.anim_player_gun_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_gun_idle.append(image)

    if anim_gun_walk is None:
        anim_gun_walk = []
        for path in asset.anim_player_gun_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_gun_walk.append(image)

    return anim_gun_attack, anim_gun_idle, anim_gun_walk

anim_knife_attack = None
anim_knife_idle = None
anim_knife_walk = None

def load_animations_player_knife():
    global anim_knife_attack, anim_knife_idle, anim_knife_walk

    if anim_knife_attack is None:
        anim_knife_attack = []
        for path in asset.anim_player_knife_attack:
            image = pygame.image.load(path).convert_alpha()
            anim_knife_attack.append(image)

    if anim_knife_idle is None:
        anim_knife_idle = []
        for path in asset.anim_player_knife_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_knife_idle.append(image)

    if anim_knife_walk is None:
        anim_knife_walk = []
        for path in asset.anim_player_knife_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_knife_walk.append(image)

    return anim_knife_attack, anim_knife_idle, anim_knife_walk


anim_item_exting = None

def load_animation_item_exting():
    global anim_item_exting

    if anim_item_exting is None:
        anim_item_exting = []
        for path in asset.anim_items_exting:
            image = pygame.image.load(path).convert_alpha()
            anim_item_exting.append(image)

    return anim_item_exting

anim_item_gun = None
anim_item_key = None
anim_item_knife = None
anim_item_molotow = None

def load_animation_item_gun():
    global anim_item_gun

    if anim_item_gun is None:
        anim_item_gun = []
        for path in asset.anim_items_gun:
            image = pygame.image.load(path).convert_alpha()
            anim_item_gun.append(image)

    return anim_item_gun

def load_animation_item_key():
    global anim_item_key

    if anim_item_key is None:
        anim_item_key = []
        for path in asset.anim_items_key:
            image = pygame.image.load(path).convert_alpha()
            anim_item_key.append(image)

    return anim_item_key

def load_animation_item_knife():
    global anim_item_knife

    if anim_item_knife is None:
        anim_item_knife = []
        for path in asset.anim_items_knife:
            image = pygame.image.load(path).convert_alpha()
            anim_item_knife.append(image)

    return anim_item_knife

def load_animation_item_molotow():
    global anim_item_molotow

    if anim_item_molotow is None:
        anim_item_molotow = []
        for path in asset.anim_items_molotow:
            image = pygame.image.load(path).convert_alpha()
            anim_item_molotow.append(image)

    return anim_item_molotow

anim_enemy_dog_idle = None
anim_enemy_dog_walk = None

def load_animation_enemy_dog():
    global anim_enemy_dog_idle, anim_enemy_dog_walk

    if anim_enemy_dog_idle is None or anim_enemy_dog_walk is None:
        anim_enemy_dog_idle = []
        anim_enemy_dog_walk = []

        for path in asset.anim_enemy_dog_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_dog_idle.append(image)

        for path in asset.anim_enemy_dog_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_dog_walk.append(image)

    return anim_enemy_dog_idle, anim_enemy_dog_walk


anim_enemy_knife_attack = None
anim_enemy_knife_idle = None
anim_enemy_knife_walk = None

def load_animation_enemy_knife():
    global anim_enemy_knife_attack, anim_enemy_knife_idle, anim_enemy_knife_walk

    if anim_enemy_knife_attack is None or anim_enemy_knife_idle is None or anim_enemy_knife_walk is None:
        anim_enemy_knife_attack = []
        anim_enemy_knife_idle = []
        anim_enemy_knife_walk = []

        for path in asset.anim_enemy_knife_attack:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_knife_attack.append(image)

        for path in asset.anim_enemy_knife_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_knife_idle.append(image)

        for path in asset.anim_enemy_knife_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_knife_walk.append(image)

    return anim_enemy_knife_attack, anim_enemy_knife_idle, anim_enemy_knife_walk


anim_enemy_gun_attack = None
anim_enemy_gun_idle = None
anim_enemy_gun_walk = None

def load_animation_enemy_gun():
    global anim_enemy_gun_attack, anim_enemy_gun_idle, anim_enemy_gun_walk

    if anim_enemy_gun_attack is None or anim_enemy_gun_idle is None or anim_enemy_gun_walk is None:
        anim_enemy_gun_attack = []
        anim_enemy_gun_idle = []
        anim_enemy_gun_walk = []

        for path in asset.anim_enemy_gun_attack:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_gun_attack.append(image)

        for path in asset.anim_enemy_gun_idle:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_gun_idle.append(image)

        for path in asset.anim_enemy_gun_walk:
            image = pygame.image.load(path).convert_alpha()
            anim_enemy_gun_walk.append(image)

    return anim_enemy_gun_attack, anim_enemy_gun_idle, anim_enemy_gun_walk

anim_active_fire = None
anim_active_smoke = None

def load_animation_effects():
    global anim_active_fire, anim_active_smoke

    if anim_active_fire is None:
        anim_active_fire = []
    if anim_active_smoke is None:
        anim_active_smoke = []

        for path in asset.anim_active_fire:
            image = pygame.image.load(path).convert_alpha()
            anim_active_fire.append(image)
        for path in asset.anim_active_smoke:
            image = pygame.image.load(path).convert_alpha()
            anim_active_smoke.append(image)

    return anim_active_fire, anim_active_smoke

human_corpses = None
dog_coprses = None

def load_corpses():
    global human_corpses, dog_coprses

    if human_corpses is None:
        human_corpses = []
    if dog_coprses is None:
        dog_coprses = []

        for path in asset.images_human_corpses:
            image = pygame.image.load(path).convert_alpha()
            human_corpses.append(image)
        for path in asset.images_dog_corpses:
            image = pygame.image.load(path).convert_alpha()
            dog_coprses.append(image)

    return human_corpses, dog_coprses