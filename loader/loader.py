import pygame
import json
import os
import entity.enemy as enemy
import entity.level as level
import entity.tile as tile
import loader.asset as asset
import loader.mapper as mapper
from entity.animation import Animation
import loader.anims as anims
from entity.item import Item
import defs.finals as finals

def read_lvl_from_json(json_path):
    try:
        with open(json_path, 'r') as lvl:
            config = json.load(lvl)
        
        layout = config['layout']
        name = config['name']
        number = config['number']
        spawn_player = config['spawn_player']
        spawn_enemies = config['spawn_enemies']
        spawn_items = config['spawn_items']
        spawn_exit = config['exit']

    except Exception as e:
        print('Error when opening {json_path}: {e}')

    return name, number, layout, spawn_player, spawn_enemies, spawn_items, spawn_exit

def init_level(json_path):
    lvl_name, lvl_number, lvl_layout, lvl_player_spawn, lvl_enemy_spawns, lvl_item_spawns, lvl_exit_spawn = read_lvl_from_json(json_path) 
    return level.Level(lvl_name, lvl_number, lvl_layout, lvl_player_spawn, lvl_enemy_spawns, lvl_item_spawns, lvl_exit_spawn)

def init_enemies(enemy_spawns, layout, tiles, group):
    enemies = []
    for row in enemy_spawns:
        pos = [row[0], row[1]]
        category = row[2]
        if category == 1:
            image = pygame.image.load(asset.image_enemy_knife).convert_alpha()
            sprites_attack, sprites_idle, sprites_walk = anims.load_animation_enemy_knife()
            animations_enemy_knife = {
                'idle': Animation(sprites_idle, 100),
                'attack': Animation(sprites_attack, 50),
                'walk': Animation(sprites_walk, 100),
            }
            animations = animations_enemy_knife
        elif category == 2:
            image = pygame.image.load(asset.image_enemy_gun).convert_alpha()
            sprites_attack, sprites_idle, sprites_walk = anims.load_animation_enemy_gun()
            animations_enemy_gun = {
                'idle': Animation(sprites_idle, 200),
                'attack': Animation(sprites_attack, 500),
                'walk': Animation(sprites_walk, 100),
            }
            animations = animations_enemy_gun
        elif category == 3:
            image = pygame.image.load(asset.image_enemy_dog).convert_alpha()
            sprites_idle, sprites_walk = anims.load_animation_enemy_dog()
            animations_enemy_dog = {
                'idle': Animation(sprites_idle, 100),
                'walk': Animation(sprites_walk, 100),
            }
            animations = animations_enemy_dog
        xy = mapper.pos_to_xy(pos, layout, tiles)
        e = enemy.Enemy(pos, xy, group, image)
        e.category = category
        e.animations = animations
        enemies.append(e)
    
    return enemies

def init_items(item_spawns, layout, tiles, group):
    items = []
    for row in item_spawns:
        pos = [row[0], row[1]]
        category = row[2]
        ammo = row[3]
        xy = mapper.pos_to_xy(pos, layout, tiles)
        if category == 1:
            image = pygame.image.load(asset.item_exting).convert_alpha()
            anim_exting = anims.load_animation_item_exting()
            animations_exting = {
            'anim': Animation(anim_exting, 100)
            }
            animations = animations_exting
            name = 'fire extinguisher'
        elif category == 2:
            image = pygame.image.load(asset.item_gun).convert_alpha()
            anim_gun = anims.load_animation_item_gun()
            animations_gun = {
            'anim': Animation(anim_gun, 100)
            }
            animations = animations_gun
            name = 'pistol'
        elif category == 3:
            image = pygame.image.load(asset.item_knife).convert_alpha()
            anim_knife = anims.load_animation_item_knife()
            animations_knife = {
            'anim': Animation(anim_knife, 100)
            }
            animations = animations_knife
            name = 'combat knife'
        elif category == 4:
            image = pygame.image.load(asset.item_molotow).convert_alpha()
            anim_molotow = anims.load_animation_item_molotow()
            animations_molotow = {
            'anim': Animation(anim_molotow, 100)
            }
            animations = animations_molotow
            name = 'molotow cocktail'
        elif category == 5:
            image = pygame.image.load(asset.item_key).convert_alpha()
            anim_key = anims.load_animation_item_key()
            animations_key = {
            'anim': Animation(anim_key, 100)
            }
            animations = animations_key
            name = 'key'
        item = Item(pos, xy, group, image)
        item.category = category
        item.ammo = ammo
        item.name = name
        item.animations = animations
        items.append(item)
    
    return items

def init_tileset(layout, camera_group):
    tiles = []
    for y, row in enumerate(layout):
        for x, layout in enumerate(row):

            filename =  asset.static_path + asset.tileset[str(layout)] 
            image = pygame.image.load(filename).convert_alpha()
            image = pygame.transform.scale(image, (finals.tile_size, finals.tile_size))
            t = tile.Tile(camera_group, image)

            t.rect.x = x * t.rect.width
            t.rect.y = y * t.rect.height
            
            t.code = layout
            t.pos[0] = x
            t.pos[1] = y

            t.init_status()

            tiles.append(t)
    
    return tiles

