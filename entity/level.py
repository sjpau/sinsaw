import os
import pygame
import sys
import loader.loader as loader
import entity.camera as camera
import entity.screen as s


codes_opaque = [1, 2]

class Level:
    def __init__(self, name, num, layout, player_spawn, enemy_spawns, item_spawns):
        self.name = name
        self.num = num
        self.layout = layout
        self.player_spawn = player_spawn
        self.enemy_spawns = enemy_spawns
        self.item_spawns = item_spawns
    
    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def get_layout(self):
        return self.layout

    def get_player_spawn(self):
        return self.player_spawn
    
    def get_enemy_spawns(self):
        return self.enemy_spawns
    
    def get_item_spawns(self):
        return self.item_spawns

def init(json_path):
    lvl_name, lvl_number, lvl_layout, lvl_player_spawn, lvl_enemy_spawns, lvl_item_spawns = loader.read_lvl_from_json(json_path) 
    return Level(lvl_name, lvl_number, lvl_layout, lvl_player_spawn, lvl_enemy_spawns, lvl_item_spawns)

def layout_to_binary(layout, codes):
    layout_binary = []
    for i in range(len(layout)):
        row = []
        for j in range(len(layout[i])):
            if layout[i][j] in codes:
                row.append(1)
            else:
                row.append(0)
        layout_binary.append(row)
    return layout_binary