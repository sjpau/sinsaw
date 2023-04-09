import os
import screen as s
import pygame
import sys
sys.path.insert(0, '../loader')
import loader
import camera

class Level:
    def __init__(self, name, num, layout, player_spawn):
        self.name = name
        self.num = num
        self.layout = layout
        self.player_spawn = player_spawn
    
    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def get_layout(self):
        return self.layout

    def get_player_spawn(self):
        return self.player_spawn

def init(json_path):
    lvl_name, lvl_number, lvl_layout, lvl_player_spawn = loader.read_lvl_from_json(json_path) 
    return Level(lvl_name, lvl_number, lvl_layout, lvl_player_spawn)

#def margin(layout, tile_size):
#    width = len(layout[0]) * (tile_size)
#    height = len(layout) * (tile_size)
#    margin_x = (s.width - width) // 2
#    margin_y = (s.height - height) // 2
    
#    return (margin_x, margin_y)