import pygame
import debug
import mapper

class GameObject:
    def __init__(self, pos):
        self.pos = pos
    
    def on_tile_index(self, layout, tiles):
        return mapper.get_tile_index_from_layout(layout, tiles, self.pos)
    
    def on_tile_collides_with(self, collider_pos, layout, tiles): # TODO: change to object
        if self.on_tile_index(layout, tiles) == mapper.get_tile_index_from_layout(layout, tiles, collider_pos):
            return True