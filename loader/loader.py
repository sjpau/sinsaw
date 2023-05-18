import pygame
import json
import os
import entity.enemy as enemy
import entity.level as level
import loader.asset as asset
import loader.mapper as mapper

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

    except Exception as e:
        print('Error when opening {json_path}: {e}')

    return name, number, layout, spawn_player, spawn_enemies, spawn_items

def init_level(json_path):
    lvl_name, lvl_number, lvl_layout, lvl_player_spawn, lvl_enemy_spawns, lvl_item_spawns = read_lvl_from_json(json_path) 
    return level.Level(lvl_name, lvl_number, lvl_layout, lvl_player_spawn, lvl_enemy_spawns, lvl_item_spawns)

def init_enemies(enemy_spawns, layout, tiles, group):
    enemies = []
    for row in enemy_spawns:
        pos = [row[0], row[1]]
        category = row[2]
        if category == 1:
            image = pygame.image.load(asset.image_enemy_dog).convert_alpha()
        elif category == 2:
            image = pygame.image.load(asset.image_enemy_gun).convert_alpha()
        xy = mapper.pos_to_xy(pos, layout, tiles)
        e = enemy.Enemy(pos, xy, group, image)
        e.category = category
        enemies.append(e)
    
    return enemies
