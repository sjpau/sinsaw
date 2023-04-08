import os
import screen as s
import pygame
import sys
sys.path.insert(0, '../loader') # TODO: orginize import the proper way
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

def custom_draw(screen, layout, tile_size, margin, camera_group, player): # TODO rewrite custom draw method to camera class
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            ### TODO here each tile will be assigned a sprite
            if layout[row][col] == 0:
                color = (255, 0, 0)
            elif layout[row][col] == 1:
                color = (0, 255, 0)
            elif layout[row][col] == 2:
                color = (0, 0, 255)
            
            rect_x =  margin[0] + col * tile_size
            rect_y =  margin[1] + row * tile_size

            camera_group.attach_to(player)
            pygame.draw.rect(screen, color, pygame.Rect(rect_x - camera_group.offset[0], rect_y - camera_group.offset[1], tile_size, tile_size))